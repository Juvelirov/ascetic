from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person, Class
from django.contrib.auth.models import Group, User


class SignUpForm(UserCreationForm):
    #group = forms.ModelMultipleChoiceField(queryset=Group.objects.all())

    class Meta:
        model = Person
        fields = ('username', 'name', 'surname', 'email', 'image', 'password1', 'password2')
        labels = {
            'username': 'Логин',
            'email': 'Email',
            'password1': 'Пароль',
            'name': 'Имя',
            'surname': 'Фамилия',
            'image': 'Фото'
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname', 'image']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия'
        }

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)


class SecurityForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['username', 'email', 'password1']
        labels = {
            'username': 'Логин',
            'email': 'Почта'
        }


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)

