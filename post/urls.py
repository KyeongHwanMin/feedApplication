from django.urls import path
from post.views import (
    PostListAPIView,
    PostListDetailAPIView,
    PostLikeAPIView,
    PostShareAPIView,
)

urlpatterns = [
    path("", PostListAPIView.as_view()),
    path("<str:pk>", PostListDetailAPIView.as_view()),
    path("likes/<str:content_id>", PostLikeAPIView.as_view()),
    path("share/<str:content_id>", PostShareAPIView.as_view()),
]
