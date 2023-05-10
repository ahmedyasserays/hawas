from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from store.models import CartItem

from .forms import CustomUserCreationForm, UserEditForm
from .models import User

admin.site.unregister(Group)


class CartItemAdmin(admin.TabularInline):
    model = CartItem
    extra: int = 0
    readonly_fields = ("total_price",)

    def total_price(self, obj):
        return obj.product.price_after_discount * obj.quantity


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    form = UserEditForm
    add_form = CustomUserCreationForm
    ordering = (
        "-start_date",
        "email",
    )
    search_fields = ("first_name", "email")
    list_display = ("email", "first_name", "is_staff")
    list_filter = ("is_staff", "is_superuser", "is_active")
    readonly_fields = ("start_date",)

    fieldsets = (
        (_("Login details"), {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name",)}),
        (
            _("Permissions"),
            {
                "fields": ("is_active", "is_staff", "is_superuser"),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "start_date")}),
        (_("Products"), {"fields": ("wishlist",)}),
    )

    filter_horizontal = ("wishlist",)

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "email",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    inlines = [CartItemAdmin]
