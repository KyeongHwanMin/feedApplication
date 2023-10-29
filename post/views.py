from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from post.models import Post
from post.serializers import PostWriteSerializer, PostListSerializer


class MyPageNumberPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_count"

    def get_page_size(self, request):
        page_count_value = request.query_params.get(self.page_size_query_param)
        if page_count_value and page_count_value.isdigit():
            return int(page_count_value)
        else:
            return self.page_size


class PostListAPIView(APIView):
    def get(self, request):
        user_id = request.user.id
        hashtag = request.query_params.get("hashtag")
        type = request.query_params.get("type")
        order_by = request.query_params.get("order_by", "created_at")
        search_by = request.query_params.get("search_by", "title,content")
        search = request.query_params.get("search")

        qs = Post.objects.all()

        if hashtag:
            qs = qs.filter(hashtags__name__iexact=hashtag, user=user_id)
        if type:
            qs = qs.filter(type=type)

        if search:
            search_query = Q()
            if "title" in search_by:
                search_query |= Q(title__icontains=search)
            if "content" in search_by:
                search_query |= Q(content__icontains=search[:20])
            qs = qs.filter(search_query)

        if order_by:
            orders_Ascending = [
                "created_at",
                "updated_at",
                "like_count",
                "share_count",
                "view_count",
            ]
            orders_descending = [
                "-created_at",
                "-updated_at",
                "-like_count",
                "-share_count",
                "-view_count",
            ]
            if order_by in orders_Ascending:
                qs = qs.order_by(order_by)
            elif order_by in orders_descending:
                qs = qs.order_by(order_by)

        paginator = MyPageNumberPagination()
        paginated_qs = paginator.paginate_queryset(qs, request)

        if paginated_qs is not None:
            serializer = PostListSerializer(paginated_qs, many=True)
            return paginator.get_paginated_response(serializer.data)
        serializer = PostListSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostWriteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


class PostListDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostListSerializer(post)
        post.view_count += 1

        post.save()
        return Response(serializer.data, status=200)


class PostLikeAPIView(APIView):
    def get_object(self, content_id):
        return get_object_or_404(Post, content_id=content_id)

    def post(self, request, content_id):
        post = self.get_object(content_id)
        post.like_count += 1
        post.save()
        return Response(status=200)
