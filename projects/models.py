from django.db import models

class Posts(models.Model):
    title= models.CharField(max_length = 100)
    page = models.ImageField()
    description = models.TextField()
    link = models.CharField(max_length = 200)
    date = models.DateField()
