from django.db import models

class Posts(models.Model):
    title= models.CharField(max_length = 100)
    image_page = models.ImageField()
    description = models.TextField()
    link = models.CharField(max_length = 200)
    date_posted = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title    
