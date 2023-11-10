from django.urls import path
from projects import views

urlpatterns = [
    path('create-proj/', views.create_project, name='create-proj'),
    path('myclass/<int:pk>/', views.class_projects, name='home'),
]