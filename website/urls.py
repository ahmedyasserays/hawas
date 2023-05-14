from django.urls import path

from .views import BlogDetailView, BlogListView, HomeView, AboutUsView, ContactUsView, ContactMessageView


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutUsView.as_view(), name="about"),
    path("blogs/", BlogListView.as_view(), name="blogs"),
    path("blog/<int:pk>/", BlogDetailView.as_view(), name="blog"),
    path("contact/", ContactMessageView.as_view(), name="contact"),    
]
