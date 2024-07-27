# in this file, we'll send a signal after user registration( post_save) so the profile will be created automatically by the receiver
from django.db.models.signals import post_save # this signal is going to be fire up; it's like a trigger after a save()
from django.contrib.auth.models import User
from django.dispatch import receiver  # dispatchers a responsible of sending signals
from .models import Profile

#in the below function,instance = user we just created  ; created = boolean value wether a user has been created or not
@receiver(post_save,sender=User)  # with this receiver "build_profile" is fired when "User" send a "post_save" signal
def build_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)   # the parameter here refers to the user we've just created


# with this receiver "build_profile" is fired when "User" send a "post_save" signal
@receiver(post_save, sender=User)
def save_profile(sender, instance,**kwargs):
    instance.profile.save()