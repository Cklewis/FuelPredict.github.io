from django.contrib import admin
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(admin.ModelAdmin):
  list_display = ('username', 'full_name', 'email')
  list_display_links = ('username', 'full_name')
  list_filter = ('full_name',)

admin.site.register(CustomUser, CustomUserAdmin)

