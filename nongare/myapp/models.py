from django.db import models

# Create your models here.
class Snippet(models.Model):
    name=models.CharField(max_length=50,blank=True)
    title = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField()


