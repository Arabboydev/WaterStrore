from django.contrib import admin
from .models import CustomUser


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'date_joined')
    list_filter = ['username', 'first_name', 'last_name', 'email', 'is_staff', 'date_joined']


admin.site.register(CustomUser, CustomUserAdmin)
