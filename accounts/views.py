from django.views.generic.base import TemplateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth import get_user_model
from .forms import RegisterForm

User = get_user_model()


# Create your views here.
class LoginView(LoginView):
    template_name = "pages/login.html"
    success_url = reverse_lazy(
        "taskmanager:task-list"
    )  # Redirect to the home page after successful login

    def form_valid(self, form):
        # You can add custom logic here if needed
        return super().form_valid(form)


class RegisterView(FormView):
    template_name = "pages/register.html"  # Template for the registration form
    form_class = RegisterForm  # Use the form we created
    success_url = reverse_lazy(
        "accounts:login"
    )  # Redirect to login page after successful registration

    def form_valid(self, form):
        # Create a new user
        email = form.cleaned_data["email"]
        password = form.cleaned_data["password"]
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]

        user = User.objects.create_user(
            username=email,  # Use email as the username
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        # Optionally, you can log the user in automatically after registration
        # from django.contrib.auth import login
        # login(self.request, user)

        return super().form_valid(form)


class ForgetPasswordView(TemplateView):
    template_name = "pages/forget-password.html"
