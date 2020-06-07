from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

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

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image_page.path)
        if img.height > 300 or img.width>300:
            output_size = (470,460)
            img.thumbnail(output_size)
            img.save(self.image_page.path)

class Rates(models.Model):
    ratings= (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)

    post = models.ForeignKey(Posts, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    design_rate = models.IntegerField(choices= ratings, default=0)
    usability_rate = models.IntegerField(choices= ratings, default=0)
    content_rate = models.IntegerField(choices= ratings, default=0)

          
