from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default = 'default.jpg', upload_to='saved')
    Bio = models.CharField(max_length = 500)

    def __str__(self):
        return f'{self.user} Profile'

