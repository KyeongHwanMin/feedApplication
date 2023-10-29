from rest_framework import serializers

from post.models import Post


class PostListSerializer(serializers.ModelSerializer):
    hashtags = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"
