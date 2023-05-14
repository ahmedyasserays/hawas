from django.views.generic import CreateView
from .forms import CustomUserCreationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.conf import settings


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy(settings.LOGIN_REDIRECT_URL)

    def form_valid(self, form):
        res = super().form_valid(form)
        login(self.request, form.instance, "django.contrib.auth.backends.ModelBackend")
        return res


class UserLoginView(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
