
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
            return Response({
                "status":"registration failed",
                "response_code":400,
                "message":"email, username, password required",
            })
            

        if User.objects.filter(email=email).exists():
            return Response({
                "status":"Email already exists",
                "response_code":400,
                "message":"Email already exists",
            })

        user = User.objects.create(
            email=email,
            username=username,
            password=make_password(password),
        )
        return Response({
                "status":"registered successfully",
                "response_code":201,
                "message":"registered successfully",
            })

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        email = request.data.get("email")
        password = request.data.get("password")

        if not email or not password:
            return Response({
                "status":"login failed",
                "response_code":400,
                "message":"email and password must be required!",   
            })
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({
                "status":"login failed",
                "response_code":401,
                "message":"invalid email or password",
            })
        
        if not user.check_password(password):
            return Response({
                "status":"login failed",
                "response_code":401,
                "message":"invalid email or password!",
            })
        

        refresh = RefreshToken.for_user(user)

        return Response({
            "status":"login success",
            "response_code":200,
            "message":"Login successful",
            "user":{
                "id":user.id,
                "email":user.email,
                "username":user.username
            },
            "token":{
                "refresh":str(refresh),
                "access": str(refresh.access_token)
            }
        })

class LogoutView(APIView):

    def post(self, request):
        refresh_token = request.data.get("refresh")

        if not refresh_token:
            return Response(
                {
                "status":"logou failed!",
                "response_code":400,
                "message":"invalid email or password!",
            }
            )

        try:
            token = RefreshToken(refresh_token)
            print(token)
            token.blacklist()
            print("hgfdedrftgyhunjkm,")
            return Response({
                
                "status":"logot completer",
                "response_code":205,
                "message":"logout succesfull",
            })
        except Exception:
                return Response({
                        "status":"Invalid refresh token",
                        "response_code":400,
                        "message":"Invalid refresh token",
                        })

