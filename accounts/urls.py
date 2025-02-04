from django.urls import include, path
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views

app_name = "accounts"

urlpatterns = [
    path("", views.LoginView.as_view(), name="login"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path("logout/", LogoutView.as_view(next_page="accounts:login"), name="logout"),
    path("about/", views.AboutView.as_view(), name="about"),
    path("contact/", views.ContactView.as_view(), name="contact"),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(
            template_name="pages/forget-password.html",  # Your forget password template
            email_template_name="pages/password_reset_email.html",  # Email template
            subject_template_name="pages/password_reset_subject.txt",  # Email subject template
            success_url="/password-reset/done/",
        ),
        name="password_reset",
    ),
    path(
        "password-reset/done/",
        auth_views.PasswordResetDoneView.as_view(
            template_name="pages/password_reset_done.html"  # Confirmation page
        ),
        name="password_reset_done",
    ),
    path(
        "password-reset-confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="pages/password_reset_confirm.html",  # Password reset form
            success_url="/password-reset/complete/",
        ),
        name="password_reset_confirm",
    ),
    path(
        "password-reset/complete/",
        auth_views.PasswordResetCompleteView.as_view(
            template_name="pages/password_reset_complete.html"  # Success page
        ),
        name="password_reset_complete",
    ),
    path("api/v1/", include("accounts.api.v1.urls")),
]
