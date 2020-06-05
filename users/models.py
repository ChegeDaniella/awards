from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default = 'default.png', upload_to='saved')
    Bio = models.CharField(max_length = 500)

    def __str__(self):
        return f'{self.user} Profile'

    def save(self):
        super().save()

        img = Image.open(self.avatar.path)
        if img.height > 300 or img.width>300:
            output_size = (400,400)
            img.thumbnail(output_size)
            img.save(self.avatar.path)



