from django.contrib import admin

from .models import Post, Hashtag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "content_id",
        "type",
        "title",
        "content",
        "view_count",
        "like_count",
        "share_count",
        "updated_at",
        "created_at",
        "user",
    )
    list_filter = ("updated_at", "created_at", "user")
    raw_id_fields = ("hashtags",)
    date_hierarchy = "created_at"


@admin.register(Hashtag)
class HashtagAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    list_filter = ("created_at",)
    search_fields = ("name",)
    date_hierarchy = "created_at"
