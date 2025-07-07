<<<<<<< HEAD
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = ['username', 'email', 'first_name', 'last_name', 'role','job_title']
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role','job_title')}),
    )

admin.site.register(Users, CustomUserAdmin)
=======
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

class CustomUserAdmin(UserAdmin):
    model = Users
    list_display = ['username', 'email', 'first_name', 'last_name', 'role','job_title']
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role','job_title')}),
    )

admin.site.register(Users, CustomUserAdmin)
>>>>>>> d7023bb44d462afe13064eb16464741bb8208045
