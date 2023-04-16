from django.db.models import (
    Max,
    Min,
    Prefetch,
    Sum,
    Case,
    When,
    Value,
    Count,
    Q,
    PositiveIntegerField,
)
from ordered_model.models import OrderedModelQuerySet
from django.http import HttpRequest


class ProductQuerySet(OrderedModelQuerySet):
    def all(self):
        return self.prefetch_related("available_sizes", "available_colors")

    def available(self):
        return self.annotate(
            sizes_count=Count("available_sizes"), color_count=Count("available_colors")
        ).filter(available=True, sizes_count__gt=0, color_count__gt=0)

    def with_images(self):
        return self.prefetch_related("images")

    def with_related_products(self, request):
        related_qs = (
            self.model.objects.available()
            .with_first_image()
            .with_first_color()
            .with_first_size()
            .with_wishlist(request)
        )
        related_products = Prefetch("related_products", queryset=related_qs)
        return self.prefetch_related(related_products)

    def with_first_image(self):
        from .models import ProductImage

        latest_imgs_pks = (
            ProductImage.objects.values("product")
            .annotate(max_id=Max("id"))
            .values_list("max_id", flat=True)
        )
        qs = self.prefetch_related(
            Prefetch(
                "images",
                queryset=ProductImage.objects.filter(pk__in=latest_imgs_pks),
                to_attr="first_image",
            )
        )
        return qs

    def with_first_color(self):
        return self.annotate(first_color=Min("available_colors"))

    def with_first_size(self):
        return self.annotate(first_size=Min("available_sizes"))

    def with_orders_count(self):
        return self.annotate(orders_count=Sum("order_items__quantity"))

    def with_wishlist(self, request: HttpRequest):
        if request.user.is_authenticated:
            return self.annotate(in_wishlist=Q(wishlist=request.user))
        else:
            wishlist_ids = request.session.get("wishlist", [])
            return self.annotate(in_wishlist=Q(id__in=wishlist_ids))

    def popular(self):
        qs = (
            self.available()
            .annotate(
                orders_count=Case(
                    When(is_popular=True, then=Value("infinity")),
                    default=Sum("order_items__quantity"),
                    output_field=PositiveIntegerField(),
                )
            )
            .order_by("-orders_count")
        )

        return qs
