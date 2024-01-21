from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator

# Create your models here.

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField(blank= True, null= True)

    def __str__(self):
        return self.title

class Answer(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    answer_text = models.TextField(blank= True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, related_name= 'answer_created_by')
    created_at = models.DateTimeField(auto_now_add=True)
    marks = models.IntegerField(null=True, blank=True, validators=[MaxValueValidator(10)])
    evaluvated_by = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, related_name= 'answer_evaluvated_by')
    evaluvated_at = models.DateTimeField(blank= True, null=True)
    remarks = models.TextField(blank= True, null=True)

    def __str__(self):
        return f"Answer to {self.assignment.title} by {self.created_by.username}"
    
