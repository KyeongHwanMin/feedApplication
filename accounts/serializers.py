import random
import re
from rest_framework import serializers

from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def validate_password(self, value):
        username = self.initial_data.get("username")
        email = self.initial_data.get("email")
        if username and username in value or email and email in value:
            raise serializers.ValidationError("다른 개인 정보와 유사한 비밀번호는 사용할 수 없습니다.")

        if len(value) < 10:
            raise serializers.ValidationError("비밀번호는 최소 10자 이상이어야 합니다.")

        common_passwords = [
            "123456",
            "password",
            "123456789",
            "12345",
            "12345678",
            "qwerty",
            "1234567",
            "111111",
            "1234567890",
            "123123",
            "abc123",
            "1234",
            "password1",
            "iloveyou",
            "1q2w3e4r",
            "000000",
            "qwerty123",
            "zaq12wsx",
            "dragon",
            "sunshine",
            "princess",
            "letmein",
            "654321",
            "monkey",
            "27653",
            "1qaz2wsx",
            "123321",
            "qwertyuiop",
            "superman",
            "asdfghjkl",
        ]
        if value in common_passwords:
            raise serializers.ValidationError("통상적으로 자주 사용되는 비밀번호는 사용할 수 없습니다.")

        if value.isdigit():
            raise serializers.ValidationError("숫자로만 이루어진 비밀번호는 사용할 수 없습니다.")

        check = 0
        if re.search(r"\d", value):
            check += 1
        if re.search(r"[a-zA-Z]", value):
            check += 1
        if re.search(r'[!@#$%^&*(),.?"{}|<>]', value):
            check += 1

        if check < 2:
            raise serializers.ValidationError("숫자, 문자, 특수문자 중 2가지 이상을 포함해야 합니다.")

        if re.search(r"(.)\1\1", value):
            raise serializers.ValidationError("3회 이상 연속되는 문자 사용이 불가합니다.")

        return value

    def create(self, validated_data):
        user = User(username=validated_data["username"], email=validated_data["email"])
        user.set_password(validated_data["password"])
        user.verification_code = "".join(random.choices("0123456789", k=6))
        user.save()
        return user

    class Meta:
        model = User
        fields = ["username", "email", "password", "verification_code"]
