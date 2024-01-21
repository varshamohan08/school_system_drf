from django.urls import path
from .views import *

app_name = 'assignment_app'

urlpatterns = [
    path('assignment', AssignmentAPI.as_view(), name='assignment'),
    path('add_assignment', AddAssignmentAPI.as_view(), name='add_assignment'),
    path('add_answer', AddAnswer.as_view(), name='add_answer'),
    path('answer', AnswerAPI.as_view(), name='answer'),
]