from rest_framework import serializers

from post.models import Post, Hashtag


class PostListSerializer(serializers.ModelSerializer):
    hashtags = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = "__all__"


class PostWriteSerializer(serializers.ModelSerializer):
    hashtags = serializers.ListField(child=serializers.CharField(), write_only=True)

    def create(self, validated_data):
        hashtag_names = validated_data.pop("hashtags")
        post = Post.objects.create(**validated_data)

        for name in hashtag_names:
            hashtag, created = Hashtag.objects.get_or_create(name=name)
            post.hashtags.add(hashtag)

        return post

    class Meta:
        model = Post
        fields = ["title", "content", "type", "hashtags", "user"]
