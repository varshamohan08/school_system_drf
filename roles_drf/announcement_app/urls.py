from django.urls import path
from .views import *

app_name = 'announcement_app'

urlpatterns = [
    path('announce', AnnouncementAPI.as_view(), name='announce'),
    path('add_announcement', AddAnnouncement.as_view(), name='add_announcement'),
]