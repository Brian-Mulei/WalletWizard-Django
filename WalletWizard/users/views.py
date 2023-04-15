from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics,status
from django.contrib.auth.models import update_last_login
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
# Class based view to Get User Details using Token Authentication
class UserDetailAPI(generics.GenericAPIView):
 # authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  serializer_class=UserSerializer
  

  def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        update_last_login(None, user)
        #token, created = Token.objects.get_or_create(user=user)
        return Response({"status": status.HTTP_200_OK,  "Data": serializer.data})

#Class based view to register user
class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer