from django.urls import path
from projects import views

urlpatterns = [
    path('create-proj/', views.create_project, name='create-proj'),
]