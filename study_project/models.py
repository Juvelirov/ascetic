from django.db import models
from django.contrib.auth.models import User


class Class(models.Model):
    name = models.CharField(max_length=10, blank=True, null=True)
    bio = models.CharField(max_length=1000, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        ordering = ['created']


class Person(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    school_class = models.OneToOneField(Class, on_delete=models.CASCADE, null=True)
    username = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    password1 = models.CharField(max_length=50, blank=True, null=True)
    password2 = models.CharField(max_length=50, blank=True, null=True)
    image = models.ImageField(blank=True, null=True, upload_to='profile_img', default='profile_img/deafult.jpg')
    created = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return str(self.username)

    class Meta:
        ordering = ['created']



