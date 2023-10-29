from django.urls import path
from post.views import PostListAPIView, PostListDetailAPIView, PostLikeAPIView

urlpatterns = [
    path("", PostListAPIView.as_view()),
    path("<str:pk>", PostListDetailAPIView.as_view()),
    path("likes/<str:content_id>", PostLikeAPIView.as_view()),
]
