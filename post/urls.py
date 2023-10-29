from django.urls import path
from post.views import PostListAPIView, PostListDetailAPIView

urlpatterns = [
    path("", PostListAPIView.as_view()),
    path("<str:pk>", PostListDetailAPIView.as_view()),
]
