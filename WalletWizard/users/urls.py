from django.urls import path
from .views import UserDetailAPI,RegisterUserAPIView
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework import routers
from . import views

router = DefaultRouter()
#router.register(r'user-details', UserUpdateAPIView, basename='user-details')
urlpatterns = [
 
 
  path("login",UserDetailAPI.as_view()),
  path('register',RegisterUserAPIView.as_view()),
]
