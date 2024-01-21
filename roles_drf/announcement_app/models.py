from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Announcement(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=255, blank= True, null= True)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null= True, related_name= 'announcement_created_by')
    created_at = models.DateTimeField(auto_now_add=True, blank= True, null= True)
    expiration_date = models.DateField(blank= True, null= True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    approved_by = models.ForeignKey(User, on_delete=models.CASCADE, blank= True, null=True, related_name= 'announcement_approved_by')
    approved_at = models.DateTimeField(blank= True, null= True)

    def __str__(self):
        return self.title
