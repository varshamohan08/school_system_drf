from django.contrib import admin
from user_app.models import UserDetails

# Register your models here.
@admin.register(UserDetails)
class UserDetailsAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'email','role','country','nationality','mobile')
    search_fields = ('user', 'name', 'email','role','country','nationality','mobile')

