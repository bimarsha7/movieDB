from django.contrib import admin
from .models import user_profile

# Register your models here.
@admin.register(user_profile)
class profile_admin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    