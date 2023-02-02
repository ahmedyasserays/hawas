from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline
from . import models
from django.db.models import Sum, Count
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.conf import settings
from django.urls import reverse


@admin.register(models.Category)
class CategoryAdmin(OrderedModelAdmin):
    list_display = [
        "name",
        "name_ar",
        "number_of_products",
        "products_of_this_category",
        "move_up_down_links",
        "order",
    ]
    readonly_fields = ['products_of_this_category']
    search_fields = ["name", "name_ar"]

    def number_of_products(self, obj):
        query_set = models.Category.objects.filter(id=obj.id).aggregate(
            Count("products")
        )
        return query_set["products__count"]


    def products_of_this_category(self, obj):
        url = reverse('admin:store_product_changelist')
        return mark_safe(
            f'<a href="{url}?category__id__exact={obj.id}" target="blank">show products</a>'
        )

    products_of_this_category.allow_tags = True


class ProductOptionsInline(OrderedTabularInline):
    model = models.Option
    extra = 1
    fields = ["name", "name_ar", "quantity", "price"]
    readonly_fields = ["move_up_down_links"]
    ordering = ("order",)


class ImagesInline(OrderedTabularInline):
    model = models.ProductImage
    extra = 1


@admin.register(models.Product)
class ProductAdmin(OrderedModelAdmin):
    list_display = [
        "name",
        "name_ar",
        "slug",
        "available",
        "created",
        "updated",
        "move_up_down_links",
        "order",
    ]
    list_filter = ["category", "available", "created", "updated"]
    list_editable = ["available"]
    search_fields = ["name", "name_ar", "slug"]
    readonly_fields = ["slug", "created", "updated", "visits"]
    filter_horizontal = ["related_products"]
    inlines = [ProductOptionsInline, ImagesInline]

    def get_urls(self):
        return (
            self.inlines[0](models.Product, self.admin_site).get_urls()
            + super().get_urls()
        )


@admin.register(models.ProductReview)
class ModelReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "product"]
