from django.urls import path

from accounts.views import UserAPIView

urlpatterns = [
    path("", UserAPIView.as_view(), name="user"),
]
