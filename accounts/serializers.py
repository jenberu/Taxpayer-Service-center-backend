from typing import Any, Dict
from rest_framework import serializers
from accounts.models import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.settings import api_settings
from django.contrib.auth.models import update_last_login
from Taxpayer.serializers import TaxPayerProfileSerializer
from Taxpayer.models import TaxPayerProfile
class UserSerializer(serializers.ModelSerializer):
    id=serializers.UUIDField(source='public_id',read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
    class Meta:
       model = User
       fields = ['id','username','is_active', 'created', 'updated', 'email', 'first_name', 'last_name', 'role']
       
       read_only_fields = ['is_active']
class RegisterSerializer(UserSerializer):
    password = serializers.CharField(max_length=128,min_length=8, write_only=True, required=True)
    profile=TaxPayerProfileSerializer()

    class Meta:
        model=User
        fields = ['id', 'bio', 'avatar', 'email',
                'username', 'first_name', 'last_name',
                'password','profile']
    def create(self, validated_data):
      #Extract taxpayer profile data
      profile_data=validated_data.pop('profile')
      user=User.objects.create_user(**validated_data)
      TaxPayerProfile.objects.create(user=user,**profile_data) 

      return user
       
      
class LoginSerializer(TokenObtainPairSerializer):
   def validate(self, attrs):
      data=super().validate(attrs)#It uses the authenticate() django built in function
      refresh=self.get_token(self.user)
      data['user']=UserSerializer(self.user).data
      data['refresh']=str(refresh)
      data['access']=str(refresh.access_token)
      if api_settings.UPDATE_LAST_LOGIN:
         update_last_login(None,self.user)
      return data   

