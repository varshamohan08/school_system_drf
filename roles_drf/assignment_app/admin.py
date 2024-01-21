from django.contrib import admin
from assignment_app.models import Answer, Assignment

# Register your models here.
@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('title','description','created_by','created_at')
    search_fields = ('title','description','created_by','created_at')

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('assignment','answer_text','created_by','created_at','marks')
    search_fields = ('assignment','answer_text','created_by','created_at','marks')