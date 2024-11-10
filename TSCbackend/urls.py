from django.contrib import admin
from django.urls import path
from rest_framework import routers
from accounts.views import UserViewSet
router=routers.DefaultRouter()
router.register(r'user',UserViewSet,basename='user')

urlpatterns = [
    path('admin/', admin.site.urls),
    *router.urls,
]
