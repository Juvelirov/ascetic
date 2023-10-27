from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Person, Class


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = instance
        Person.objects.create(user=user,
                              username=user.username,
                              email=user.email,
                              password1=user.password,
                              password2=user.password)


post_save.connect(create_profile, sender=User)