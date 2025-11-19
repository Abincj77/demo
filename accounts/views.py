
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


User = get_user_model()


class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        email = request.data.get("email")
        username = request.data.get("username")
        password = request.data.get("password")

        if not email or not password or not username:
            return Response({"error": "email, username, password required"},
                            status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"},
                            status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create(
            email=email,
            username=username,
            password=make_password(password),
        )

        return Response({"message": "User registered successfully"},
                        status=status.HTTP_201_CREATED)

class LoginView(TokenObtainPairView):
    pass  # no custom serializer needed


class LogoutView(APIView):

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {"detail": "Refresh token is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # try:
        token = RefreshToken(refresh_token)
        print(token)
        token.blacklist()
        print("hgfdedrftgyhunjkm,")
        return Response(
            {"detail": "Logout successful"},
            status=status.HTTP_205_RESET_CONTENT
        )
        # return Response("hai")
        # except Exception:
        #     return Response(
        #         {"detail": "Invalid refresh token"},
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
