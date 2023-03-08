from django.urls import path
from . import views


urlpatterns = [
    path("",views.Home.as_view(),name='home'),
    path("api/wishlist/",views.WishList_ListCreateApiView.as_view()),
]
