from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Person, Class
from django.contrib.auth.models import Group, User
from django.contrib.auth import get_user_model


class SignUpForm(UserCreationForm):
    group = forms.ModelMultipleChoiceField(queryset=Group.objects.all())

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        labels = {
            'username': 'Логин',
            'email': 'Email',
            'password1': 'Пароль',
            'password2': 'Повторите пароль'
        }

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'surname']
        labels = {
            'name': 'Имя',
            'surname': 'Фамилия'
        }

    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)


class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ('name', 'bio')

    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)

