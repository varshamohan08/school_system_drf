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
    

{
    "title": "Research Paper: Artificial Intelligence in Healthcare",
    "description": "Write a research paper discussing the applications, challenges, and future prospects of integrating artificial intelligence into healthcare systems.",
    "due_date": "2024-03-15"
}

{
    "assignment": "2",
    "answer_text": "For the Mathematics Project, I delved into the mesmerizing world of fractals and chaos theory. I created visual representations of famous fractals such as the Mandelbrot set and explored their self-replicating patterns. Additionally, I provided detailed explanations of the underlying mathematical principles behind these phenomena. To demonstrate real-world applications, I discussed how fractals and chaos theory are employed in fields like computer graphics, weather prediction, and finance. The project was an enlightening journey into the profound beauty and practical significance of these mathematical concepts."
}
{
    "assignment": "1",
    "answer_text": "In the Web Development assignment, I built a fully functional e-commerce website using Django and React. The website includes features such as user authentication, product catalog, shopping cart, and order processing. The frontend is designed with a responsive and intuitive user interface. Throughout the development process, I followed best practices, utilized RESTful APIs, and ensured the security of user data. Overall, the project was a great opportunity to apply theoretical knowledge to practical implementation.",
}

{
    "id" : "1",
    "marks": "10",
    "remarks": "Good"
}