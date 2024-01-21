from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    ROLE_CHOICES = [
        ('Student', 'Student'),
        ('Staff', 'Staff'),
        ('Admin', 'Admin'),
        ('Editor', 'Editor'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user_details')
    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, null=True)
    country = models.CharField(max_length=50, blank=True)
    nationality = models.CharField(max_length=50, blank=True)
    mobile = models.CharField(max_length=15, unique= True)

    def __str__(self):
        print(f"Calling __str__ for {self.user.username}'s Details")
        return f"{self.user.username}'s Details"
