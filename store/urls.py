from django.urls import path

from .views import AddToAndRemoveFromWishlistView, CartItemsCountView, CartView, ProductDetailView, AddToCartView

urlpatterns = [
    path("shop/cart/", CartView.as_view(), name="cart"),
    path("shop/<slug:slug>/", ProductDetailView.as_view(), name="product_details"),
    path("api/wishlist/<int:prod_id>/", AddToAndRemoveFromWishlistView.as_view(), name="update_wishlist"),
    path("api/cart/", AddToCartView.as_view(), name="add_to_cart"),
    path("api/cart/count/", CartItemsCountView.as_view(), name="cart_items_count"),
]
