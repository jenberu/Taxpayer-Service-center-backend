from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .serializers import UserSerializer
from .models import User
from django.http import Http404

from rest_framework.pagination import PageNumberPagination
class CustomPagination(PageNumberPagination):
    page_size = 10 
class UserViewSet(viewsets.ModelViewSet):
    http_method_names=('patch','get')
    permission_classes=[AllowAny]
    serializer_class=UserSerializer
    pagination_class=CustomPagination

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()
        return User.objects.exclude(is_superuser=True)
    def get_object(self):
        try:
            obj = User.objects.get_object_by_public_id(self.kwargs['pk'])
            return obj
        except Http404:
            raise Http404("User with this public ID does not exist.")


