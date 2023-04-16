from django.views.generic import DetailView
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from store.models import Product, CartItem
from store.managers import ProductQuerySet

# Create your views here.


class ProductDetailView(DetailView):
    model = Product
    template_name = "store/product_details.html"
    context_object_name = "product"

    def get_queryset(self):
        qs: ProductQuerySet = super().get_queryset()
        qs = qs.available().with_images().with_related_products(self.request)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            ctx["in_wishlist"] = self.request.user.wishlist.filter(
                id=self.object.id
            ).exists()
        else:
            ctx["in_wishlist"] = self.object.id in self.request.session.get(
                "wishlist", set()
            )
        return ctx


class AddToAndRemoveFromWishlistView(APIView):
    http_method_names = ["post", "delete"]

    def post(self, request, prod_id):
        user = self.request.user
        obj = get_object_or_404(Product, id=prod_id)
        if user.is_authenticated:
            user.wishlist.add(obj)
        else:
            wishlist = set(self.request.session.get("wishlist", []))
            wishlist.add(prod_id)
            self.request.session["wishlist"] = list(wishlist)
            self.request.session.modified = True
        return Response({"success": True})

    def delete(self, request, prod_id):
        user = self.request.user
        if user.is_authenticated:
            user.wishlist.remove(prod_id)
        else:
            wishlist = set(self.request.session.get("wishlist", []))
            wishlist.remove(prod_id)
            self.request.session["wishlist"] = list(wishlist)
            self.request.session.modified = True
        return Response({"success": True})


class AddToCartView(CreateAPIView):
    class AddToCartSerializer(serializers.ModelSerializer):
        class Meta:
            model = CartItem
            exclude = ["user"]

    serializer_class = AddToCartSerializer

    def post(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return super().post(self.request)
        else:
            cart = set(self.request.session.get("cart", []))
            ser = self.serializer_class(data=self.request.data)
            ser.is_valid(raise_exception=True)
            
            self.request.session["cart"] = list(cart)
            self.request.session.modified = True
        return Response({"success": True})

    def perform_create(self, serializer):
        cart_item = CartItem.objects.filter(
            user=self.request.user,
            product=serializer.validated_data["product"],
            color=serializer.validated_data["color"],
            size=serializer.validated_data["size"],
        ).first()
        if cart_item:
            cart_item.quantity += serializer.validated_data["quantity"]
            cart_item.save()
        else:
            serializer.save(user=self.request.user)

