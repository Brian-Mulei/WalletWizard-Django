from django.urls import path
from .views import CategoryList,CategoryByUser,CategoryDetail
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from rest_framework import routers
from . import views

router = DefaultRouter()
#router.register(r'user-details', UserUpdateAPIView, basename='user-details')
urlpatterns = [
 
 
path("Category_list",CategoryList.as_view()),
path('Category_by_User',CategoryByUser.as_view()),
path('Category_Detail',CategoryDetail.as_view()),

]
