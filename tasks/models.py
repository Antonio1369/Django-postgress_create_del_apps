from django.db import models

# Create your models here.

class Task(models.Model):
    titulo = models.CharField(max_length=100)
    foundation = models.TextField(blank=True) #texto opcional, no es necesario añardirlo