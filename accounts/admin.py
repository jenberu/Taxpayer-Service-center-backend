from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
class CustomUserAdmin(admin.ModelAdmin):
    # Fields to be displayed on the list page in the admin
    list_display = ('email','username', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'created', 'updated')

admin.site.register(User, CustomUserAdmin)
