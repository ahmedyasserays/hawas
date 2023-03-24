from django.urls import path

from .views import AddToAndRemoveFromWishlistView, ProductDetailView

urlpatterns = [
    path("<slug:slug>/", ProductDetailView.as_view(), name="product_detail"),
    path("api/wishlist/<int:prod_id>/", AddToAndRemoveFromWishlistView.as_view()),
]
