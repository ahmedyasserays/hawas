from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect



class RegisterView(CreateView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")


class UserLoginView(LoginView):
    template_name = "login.html"
    success_url = reverse_lazy("home")

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect(self.get_success_url())
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        username = email
        return super().form_valid(form)