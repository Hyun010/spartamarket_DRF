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

@api_view(["POST"])
def signup(request):
    serializer=RegisterSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    
@api_view(["POST"])
def login(request):
    username=request.data['username']
    password=request.data['password']
    user=User.objects.filter(username=username).first()
    serialize_user=loginSerializer(user)
    json_user=JSONRenderer().render(serialize_user.data)
    if user is None :
        raise AuthenticationFailed('User does not found!')
    if not user.check_password(password) :
        raise AuthenticationFailed("Incorrect password!")
    payload = {
        'id' : user.id,
        'exp' : datetime.datetime.now() + datetime.timedelta(minutes=60),
        'iat' : datetime.datetime.now()
    }
    token = jwt.encode(payload,"secretJWTkey",algorithm="HS256")
    res = Response()
    res.set_cookie(key='jwt', value=token, httponly=True)
    res.data = {
        'jwt' : token
    }
    return res

class ProfileAPIView(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request,username):
        user = get_object_or_404(User, username=username)
        serializer = profileSerializer(user)
        return Response(serializer.data)