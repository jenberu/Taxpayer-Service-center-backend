from django.urls import path,include
from rest_framework import routers
from .views import UserViewSet ,RegisterViewSet
router=routers.DefaultRouter()
router.register(r'user',UserViewSet,basename='user')
router.register(r'register', RegisterViewSet,basename='register')
urlpatterns = [
    path('',include(router.urls)),
]