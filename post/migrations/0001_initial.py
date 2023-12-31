# Generated by Django 4.2.6 on 2023-10-29 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Hashtag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, unique=True)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("content_id", models.CharField(max_length=255, verbose_name="id")),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("facebook", "facebook"),
                            ("twitter", "twitter"),
                            ("instagram", "instagram"),
                            ("threads", "threads"),
                        ],
                        max_length=15,
                        verbose_name="유형",
                    ),
                ),
                ("title", models.CharField(max_length=255, verbose_name="제목")),
                ("content", models.TextField(verbose_name="내용")),
                (
                    "view_count",
                    models.PositiveIntegerField(default=0, verbose_name="조회 수"),
                ),
                (
                    "like_count",
                    models.PositiveIntegerField(default=0, verbose_name="좋아요 수"),
                ),
                (
                    "share_count",
                    models.PositiveIntegerField(default=0, verbose_name="공유 수"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="수정 날짜"),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="생성 날짜"),
                ),
                ("hashtags", models.ManyToManyField(blank=True, to="post.hashtag")),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="post",
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="작성자",
                    ),
                ),
            ],
        ),
    ]
