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
{
    "username" : "Admin1",
    "password" : "test@123"
}
{
    "name" : "Admin 1",
    "username" : "Admin1",
    "password" : "test@123",
    "email" : "admin1@test.com",
    "role" : "Admin",
    "country" : "India",
    "nationality" : "Indian",
    "mobile" : "9999988888"
}
{
    "name" : "Staff 1",
    "username" : "Staff1",
    "password" : "test@123",
    "email" : "Staff1@test.com",
    "role" : "Staff",
    "country" : "India",
    "nationality" : "Indian",
    "mobile" : "9999988887"
}
{
    "name" : "Student 1",
    "username" : "Student1",
    "password" : "test@123",
    "email" : "Student1@test.com",
    "role" : "Student",
    "country" : "India",
    "nationality" : "Indian",
    "mobile" : "9999988886"
}
{
    "name" : "Editor 1",
    "username" : "Editor1",
    "password" : "test@123",
    "email" : "Editor1@test.com",
    "role" : "Editor",
    "country" : "India",
    "nationality" : "Indian",
    "mobile" : "9999988886"
}