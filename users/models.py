from django.db import models
from django.contrib.auth.models import User
from PIL import Image


# Create your models here.
class Profile(models.Model):
    # each user has a profile and each profile belongs to a user. 
    # Therefore, the relationship between the User model and the 
    # Profile model is one-to-one.
    # If a User is deleted, the Profile associated with the User
    # is also deleted, thus indicates on_delete=models.CASCADE
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='avatar.jpg', upload_to='profile_avatars')
    
    def __str__(self) -> str:
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        # save the profile first
        super().save(*args, **kwargs)
        
        img = Image.open(self.avatar.path)
        # resize the iamge
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            # create a thumbnail
            img.thumbnail(output_size)
            img.save(self.avatar.path)