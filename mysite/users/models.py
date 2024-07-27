from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE) # this means , if you delete a User, also delete the profile associated
    # below fields will be accessed using  "user.profile.image or user.profile.location"
    image = models.ImageField(default='profilepic.jpg', upload_to ='profile_pictures') # upload_to = equal the directory where the default file is located
    location = models.CharField(max_length=100)

    #representation of the model which means what we want to print when we access the model

    def __str__(self):
        return self.user.username