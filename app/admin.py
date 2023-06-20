from django.contrib import admin
from .models import *

# Register your models here.

@admin.register((Registration))
class RegistrationModeladmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password','contact']
    
@admin.register((Courses))
class CoursesModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'name','fees', 'duration', 'comments']
    
    