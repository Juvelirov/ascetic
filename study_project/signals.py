from django.contrib.auth.models import User, Group
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


# @receiver(user_registered, sender=User)
# def user_registered_callback(sender, user, request, **kwargs):
#     group_name = request.POST.get('Teacher')
#     group = Group.objects.get(name=group_name)
#     user.groups.add(group)


post_save.connect(create_profile, sender=User)
# user_registered.connect(user_registered_callback, sender=User)
