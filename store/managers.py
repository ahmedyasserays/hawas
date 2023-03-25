from django.db.models import (
    Max,
    Min,
    Prefetch,
    Sum,
    Case,
    When,
    Value,
    PositiveIntegerField,
)
from ordered_model.models import OrderedModelQuerySet


class ProductQuerySet(OrderedModelQuerySet):
    def available(self):
        return self.filter(available=True)

    def with_options(self):
        return self.prefetch_related("options")

    def with_images(self):
        return self.prefetch_related("images")
    
    def with_related_products(self):
        related_qs = self.model.objects.available().with_first_image().with_price()
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

    def with_orders_count(self):
        return self.annotate(orders_count=Sum("options__order_items__quantity"))

    def with_price(self):
        return self.annotate(price=Min("options__price"))

    def popular(self):
        qs = (
            self.available()
            .annotate(
                orders_count=Case(
                    When(is_popular=True, then=Value("infinity")),
                    default=Sum("options__order_items__quantity"),
                    output_field=PositiveIntegerField(),
                )
            )
            .order_by("-orders_count")
        )

        return qs
