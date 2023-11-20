from django.contrib import admin

from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "password",
        "last_login",
        "verification_code",
        "id",
        "email",
        "username",
        "is_active",
        "is_admin",
    )
    list_filter = ("last_login", "is_active", "is_admin")
