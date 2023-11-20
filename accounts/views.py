from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import User
from accounts.serializers import UserSerializer


class UserAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserVerificationView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")
        verification_code = request.data.get("verification_code")

        try:
            user = User.objects.get(username=username)

            if not user.check_password(password):
                return Response("비밀번호가 일치하지 않습니다.", status=status.HTTP_400_BAD_REQUEST)

            if user.verification_code != verification_code:
                return Response("인증번호가 일치하지 않습니다.", status=status.HTTP_400_BAD_REQUEST)

            user.is_active = True
            user.verification_code = None
            user.save()

            return Response("회원가입이 승인되었습니다.", status=status.HTTP_200_OK)

        except User.DoesNotExist:
            return Response("없는 계정입니다.", status=status.HTTP_400_BAD_REQUEST)
