from django.urls import path

from .views import HomeView, AboutUsView, ContactUsView, ContactMessageView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutUsView.as_view(), name="about"),
    path("contact/", ContactUsView.as_view(), name="contact"),
    path("send/", ContactMessageView.as_view(), name="send"),
    
    
]
