from django.urls import include, path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView

app_name = "accounts"

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("forget-password/", views.ForgetPasswordView.as_view(), name="forget-password"),
    path('logout/', LogoutView.as_view(next_page='accounts:login'), name='logout'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]
