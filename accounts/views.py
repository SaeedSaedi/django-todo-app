from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class LoginView(TemplateView):
    template_name = "pages/login.html"


class RegisterView(TemplateView):
    template_name = "pages/register.html"


class ForgetPasswordView(TemplateView):
    template_name = "pages/forget-password.html"
