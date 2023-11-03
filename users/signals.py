from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    """
    Creates a new profile after a User object is created.

    Parameters:
        sender (Any): The sender of the signal.
        instance (User): The instance of the User model.
        created (bool): A boolean indicating if the user was created.
        **kwargs (Any): Additional keyword arguments.

    Returns:
        None
    """
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    """
    Saves the profile of a user after A User object is saved.

    Parameters:
        sender (Any): The sender of the signal.
        instance (User): The user instance that has been saved.
        **kwargs (Any): Additional keyword arguments.

    Returns:
        None
    """
    instance.profile.save()