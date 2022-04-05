from email.policy import default
from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=50)
    message = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.name} - {self.subject}'

class Projects(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    technologies = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media')
    video_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    date = models.DateField()

    def __str__(self):
        return self.title

