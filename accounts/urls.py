from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView

from accounts.views import UserAPIView, UserVerificationView

urlpatterns = [
    path("", UserAPIView.as_view(), name="user"),
    path("token", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("verification", UserVerificationView.as_view(), name="user_verification"),
]
