from django import forms
from django.contrib.admin.widgets import FilteredSelectMultiple
from store.models import Product
from django.forms import widgets


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "available_colors": widgets.CheckboxSelectMultiple(),
            "available_sizes": widgets.CheckboxSelectMultiple(),
            "related_products": FilteredSelectMultiple("Related Products", False),
        }
