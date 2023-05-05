import django_filters as filters
from store.models import Product
from django.db.models import Q

class ProductFilter(filters.FilterSet):
    prod_name = filters.CharFilter(method="prod_name_filter")

    class Meta:
        model = Product
        fields = {
            "price": ["gte", "lte"],
            "category": ["exact"],
        }

    def prod_name_filter(self, qureyset, name, value):
        return qureyset.filter(Q(name__icontains=value)| Q(name_ar__icontains=value))
    
