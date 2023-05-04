import django_filters as filters
from store.models import Product


class ProductFilter(filters.FilterSet):
    prod_name = filters.CharFilter(method="prod_name_filter")

    class Meta:
        model = Product
        fields = {
            "price": ["exact", "gte", "lte"],
            "category": ["exact"],
        }

    def prod_name_filter(self, qureyset, name, value):
        print(name, value)
        return qureyset
