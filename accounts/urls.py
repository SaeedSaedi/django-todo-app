from django.urls import include, path
from . import views
from django.views.generic import TemplateView

app_name = "accounts"

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
]
