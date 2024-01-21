from django.urls import path
from .views import *

app_name = 'user_app'

urlpatterns = [
    path('reg_form', userRegistration.as_view(), name='reg_form'),
    path('user_api', userCommonApi.as_view(), name='user_api'),
    path('user_list', userApi.as_view(), name='user_list'),
    path('login', userLogin.as_view(), name='login'),
    path('logout', userLogout.as_view(), name='logout'),
]