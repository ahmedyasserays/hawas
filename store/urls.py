from django.urls import path

from .views import AddToAndRemoveFromWishlistView, ProductDetailView, AddToCartView

urlpatterns = [
    path("shop/<slug:slug>/", ProductDetailView.as_view(), name="product_details"),
    path("api/wishlist/<int:prod_id>/", AddToAndRemoveFromWishlistView.as_view(), name="update_wishlist"),
    path("api/cart/", AddToCartView.as_view(), name="add_to_cart"),
]
