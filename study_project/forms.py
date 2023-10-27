from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person, Class
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta:
        model = Person
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('name', 'bio')

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)

