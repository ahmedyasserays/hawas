from django.contrib import admin
from .forms import CustomUserCreationForm, UserEditForm
from .models import  User,CartItem
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group

admin.site.unregister(Group)

class CartItemAdmin(admin.TabularInline):
    model = CartItem
    extra: int = 0
    readonly_fields = ("price", )
    
    def price(self, obj):
        return obj.option.price*obj.quantity

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    form = UserEditForm
    add_form = CustomUserCreationForm
    ordering = ('-start_date', 'email',)
    search_fields = ('first_name', 'last_name', 'email')
    list_display = ('email', 'first_name', 'last_name', 'is_staff')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    readonly_fields = ('start_date',)

    fieldsets = (
        (_('Login details'), {'fields': ('email', 'password')}),
        (_('Personal info'), {'fields': (
                                        'first_name', 'last_name')}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'start_date')}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    inlines = [CartItemAdmin]
