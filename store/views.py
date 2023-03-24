from django.http import JsonResponse
from django.views import View
from django.views.generic import DetailView
from django.shortcuts import get_object_or_404

from store.models import Product
from store.managers import ProductQuerySet

# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_detail.html"
    context_object_name = "product"

    def get_queryset(self):
        qs: ProductQuerySet = super().get_queryset()
        qs = qs.available().with_images().with_options().with_related_products()
        return qs


class AddToAndRemoveFromWishlistView(View):
    http_method_names = ["post", "delete"]

    def post(self, request, prod_id):
        user = request.user
        obj = get_object_or_404(Product, id=prod_id)
        if user.is_authenticated:
            user.wishlist.add(obj)
        else:
            wishlist = request.session.get("wishlist", set())
            wishlist.add(prod_id)
            request.session["wishlist"] = wishlist
            request.session.modified = True
        return JsonResponse({"success": True})

    def delete(self, request, prod_id):
        user = request.user
        if user.is_authenticated:
            user.wishlist.remove(prod_id)
        else:
            wishlist = request.session.get("wishlist", set())
            wishlist.remove(prod_id)
            request.session["wishlist"] = wishlist
            request.session.modified = True
        return JsonResponse({"success": True})
