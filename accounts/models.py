import uuid
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from .customManagers import UserManager
from AdminLevel.models import Kebele
class User(AbstractBaseUser, PermissionsMixin):
   ROLE_CHOICES=[
        ('TAXPAYER', 'Taxpayer'),
        ('KEBELE_ADMIN', 'Kebele Admin'),
        ('WOREDA_ADMIN', 'Woreda Admin'),
        ('ZONE_ADMIN', 'Zone Admin'),
        ('REGIONAL_ADMIN', 'Regional Admin'),
   ]
   public_id = models.UUIDField(db_index=True, unique=True, default=uuid.uuid4, editable=False)
   username = models.CharField(db_index=True,max_length=255, unique=True)
   first_name = models.CharField(max_length=255)
   last_name = models.CharField(max_length=255)
   role=models.CharField(max_length=30,choices=ROLE_CHOICES,default="TAXPAYER")
   email=models.EmailField(db_index=True,unique=True,)
   is_active=models.BooleanField(default=True)
   is_staff = models.BooleanField(default=False)
   created=models.DateTimeField(auto_now_add=True)
   updated=models.DateTimeField(auto_now=True)
   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['username']
   objects=UserManager()
   def __str__(self):
       return f"{self.username}"
   @property
   def name(self):
       return f"{self.first_name} {self.last_name}"

      
      
   
