from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    RegisterAPIView,
    LoginAPIView,
    LogoutAPIView,
    PasswordResetAPIView,
    JWTAuthLoginAPIView,
)

app_name = "accounts_api"

urlpatterns = [
    path("register/", RegisterAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),
    path("logout/", LogoutAPIView.as_view(), name="logout"),
    path("password-reset/", PasswordResetAPIView.as_view(), name="password_reset"),
    # JWT Authentication URLs
    path("jwt/login/", JWTAuthLoginAPIView.as_view(), name="jwt_login"),
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("token/verify/", TokenVerifyView.as_view(), name="token_verify"),
]
