from django.urls import path
from study_project import views

urlpatterns = [
    path('', views.registration),
    path('login/', views.user_login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('myclass/', views.class_create, name='class'),
    path('edit_account/', views.edit_profile, name='edit_profile')
]