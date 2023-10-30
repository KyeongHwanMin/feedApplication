from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError("이메일을 입력해 주세요.")

        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None):
        user = self.create_user(email, password=password, username=username)
        user.is_admin = True
        user.is_staff = True
        user.is_active = True

        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    verification_code = models.CharField(max_length=6, blank=True, null=True)

    id = models.AutoField(primary_key=True)
    email = models.EmailField(
        default="", max_length=100, null=False, blank=False, unique=True
    )
    username = models.CharField(
        default="", max_length=100, null=False, blank=False, unique=True
    )

    is_active = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
