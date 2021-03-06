from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image

class Posts(models.Model):
    title= models.CharField(max_length = 100)
    image_page = models.ImageField(upload_to='imgpro/')
    description = models.TextField()
    link = models.URLField (max_length = 200)
    date_posted = models.DateField(auto_now_add=True)
    designer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title    

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk}) 

    def save_posts(self):
        self.save()    

    def delete_posts(self):
        self.delete()  

    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image_page.path)
        if img.height > 300 or img.width>300:
            output_size = (470,460)
            img.thumbnail(output_size)
            img.save(self.image_page.path)

    @classmethod
    def search_by_title(cls,search_term):
        title = cls.objects.filter(title__icontains = search_term)
        return title

    @property
    def design_rate(self):
       if self.votes.count() == 0:
           return 5
       return sum([r.design_rate for r in self.votes.all()]) / self.votes.count()   

    @property
    def usability_rate(self):
       if self.votes.count() == 0:
           return 5
       return sum([r.usability_rate for r in self.votes.all()]) / self.votes.count()     

    @property
    def content_rate(self):
       if self.votes.count() == 0:
           return 5
       return sum([r.content_rate for r in self.votes.all()]) / self.votes.count()   
          


class Rates(models.Model):
    ratings= (1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10)

    post = models.ForeignKey(Posts, related_name='votes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    design_rate = models.IntegerField(choices= ratings, default=0)
    usability_rate = models.IntegerField(choices= ratings, default=0)
    content_rate = models.IntegerField(choices= ratings, default=0)

 

    def save_rates(self):
        self.save()

    def delete_rates(self):
        self.delete()    

    def get_absolute_url(self):
        return reverse('posts')    


          
