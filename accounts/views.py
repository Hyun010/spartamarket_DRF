from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view
from .serializers import RegisterSerializer,loginSerializer,profileSerializer
from rest_framework.response import Response
from rest_framework import status
from .models import User
from rest_framework.renderers import JSONRenderer
from rest_framework.exceptions import AuthenticationFailed
import jwt,datetime
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .permissions import CustomReadOnly

@api_view(["POST"])
def signup(request):
    serializer=RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
class LoginAPI(APIView):
    def post(self,request):
        usernaem=request.data['username']
        password=request.data['password']

        user=User.objects.filter(username=usernaem).first()
        if user is None:
            return Response({"message":"존재하지 않는 아이디입니다."},status=status.HTTP_400_BAD_REQUEST)
        if not check_password(password,user.password):
            return Response({"message":"비밀번호 틀립니다."},status=status.HTTP_400_BAD_REQUEST)
        if user is not None:
            token=TokenObtainPairSerializer.get_token(user)
            refresh_token=str(token)
            access_token=str(token.access_token)
            response=Response(
                {
                    'user' : profileSerializer(user).data,
                    "jwt_token" : {
                        "access_token" : access_token,
                        "refresh_token" : refresh_token
                    },
                },
            status=status.HTTP_200_OK
            )
            response.set_cookie("access_token", access_token, httponly=True)
            response.set_cookie("refresh_token", refresh_token, httponly=True)
            return response
        else:
            return Response({"message":"로그인 실패입니다."},status=status.HTTP_400_BAD_REQUEST)


class ProfileAPIView(APIView):
    permission_classes=[CustomReadOnly]

    def get(self, request,username):
        user = get_object_or_404(User, username=username)
        if request.user==user:
            serializer = profileSerializer(user)
            return Response(serializer.data)
        else:
            return Response({"message":"잘못된 접근입니다."},status=status.HTTP_400_BAD_REQUEST)