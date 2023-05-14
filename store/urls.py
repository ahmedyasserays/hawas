from django.urls import path

from .views import (
    AddToAndRemoveFromWishlistView,
    AddToCartView,
    CartItemsCountView,
    CartView,
    ProductDetailView,
    ShopView,
    decrement_cart_quantity,
)

urlpatterns = [
    path(
        "api/wishlist/<int:prod_id>/",
        AddToAndRemoveFromWishlistView.as_view(),
        name="update_wishlist",
    ),
    path(
        "api/cart/",
        AddToCartView.as_view(),
        name="add_to_cart",
    ),
    path(
        "api/cart/count/",
        CartItemsCountView.as_view(),
        name="cart_items_count",
    ),
    path(
        "api/cart/<int:id>/decrement/",
        decrement_cart_quantity,
        name="decrement_cart_quantity",
    ),
    path(
        "shop/cart/",
        CartView.as_view(),
        name="cart",
    ),
    path(
        "shop/",
        ShopView.as_view(),
        name="shop",
    ),
    path(
        "shop/<slug:slug>/",
        ProductDetailView.as_view(),
        name="product_details",
    ),
]
