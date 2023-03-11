from django.urls import path

from .views import AddToAndRemoveFromWishlistView

urlpatterns = [
    path("api/wishlist/", AddToAndRemoveFromWishlistView.as_view()),
]
