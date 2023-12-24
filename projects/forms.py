from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('description', 'image')
        labels = {
            'title': 'Название',
            'description': 'Описание',
            'image': 'Превью'
        }

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)