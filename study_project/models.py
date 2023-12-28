from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User, Group
from django.conf import settings
import uuid


class Class(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']


class Person(AbstractUser):
    #user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    school_class = models.ForeignKey(Class, on_delete=models.CASCADE, null=True)
    #username = models.CharField(max_length=50, unique=True, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    #email = models.EmailField(max_length=100, blank=True, null=True)
    password1 = models.CharField(max_length=50, blank=True, null=True)
    password2 = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile_img', default='profile_img/avatars.svg')
    created = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    #USERNAME_FIELD = 'username'

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']

