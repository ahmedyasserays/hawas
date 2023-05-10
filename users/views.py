from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

class RegisterView(CreateView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("home")
