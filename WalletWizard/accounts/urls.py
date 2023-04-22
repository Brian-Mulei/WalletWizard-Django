from django.urls import path
from .views import AccountListCreateView,AccountRetrieveUpdateDestroyView
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework import routers
 
router = DefaultRouter()
#router.register(r'user-details', UserUpdateAPIView, basename='user-details')
urlpatterns = [
 
 
  path("ACC",AccountListCreateView.as_view()),
  path('Accounts',AccountRetrieveUpdateDestroyView.as_view()),
]
