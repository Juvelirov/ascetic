# Generated by Django 4.2.6 on 2023-12-12 11:26

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('title', models.CharField(blank=True, max_length=70, null=True)),
                ('description', models.CharField(blank=True, max_length=1000, null=True)),
                ('image', models.ImageField(blank=True, default='project_img/default', null=True, upload_to='project_img')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
