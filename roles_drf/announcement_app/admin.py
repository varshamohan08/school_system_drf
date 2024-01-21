from django.contrib import admin
from announcement_app.models import Announcement

# Register your models here.
@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title','content','created_by','created_at','expiration_date','status','approved_by','approved_at')
    search_fields = ('title','content','created_by','created_at','expiration_date','status','approved_by','approved_at')

