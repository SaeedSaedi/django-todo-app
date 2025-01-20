from django.urls import include, path
from . import views
from django.views.generic import TemplateView

app_name = "accounts"

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("forget-password/", views.ForgetPasswordView.as_view(), name="forget-password"),
]
