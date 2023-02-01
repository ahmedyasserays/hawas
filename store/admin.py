from django.contrib import admin
from ordered_model.admin import OrderedModelAdmin, OrderedTabularInline
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name","name_ar"]
    search_fields = ['name','name_ar']
    
    
    
class OrderOptionsInline(OrderedTabularInline):
    model = models.Option
    extra = 1
    fields = ["name", "name_ar", "quantity", "price", "discount", "move_up_down_links"]
    readonly_fields = ["move_up_down_links"]
    ordering = ("order",)



class ImagesInline(admin.StackedInline):
    model = models.ProductImage
    extra = 1
    


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "name_ar", "slug", "available", "created", "updated"]
    list_filter = ["category", "available", "created", "updated"]
    list_editable = ["available"]
    search_fields = ["name", "name_ar", "slug"]
    readonly_fields = ["slug", "created", "updated", "visits"]
    filter_horizontal = ["related_products"]
    inlines = [OrderOptionsInline, ImagesInline]

    def get_urls(self):
        return self.inlines[0](models.Product, self.admin_site).get_urls() + super().get_urls()


@admin.register(models.ProductReview)
class ModelReviewAdmin(admin.ModelAdmin):
    list_display = ["user","product"]
