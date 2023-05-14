from django.urls import path

from .views import HomeView, AboutUsView, ContactMessageView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutUsView.as_view(), name="about"),
    path("contact/", ContactMessageView.as_view(), name="contact"),    
    
]
