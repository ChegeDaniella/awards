from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Posts(models.Model):
    title= models.CharField(max_length = 100)
    image_page = models.ImageField(upload_to='imgpro/')
    description = models.TextField()
    link = models.CharField(max_length = 200)
    date_posted = models.DateField(auto_now_add=True)
    designer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk}) 

    def save_posts(self):
        self.save()    


