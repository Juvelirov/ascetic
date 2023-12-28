from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project
from study_project.models import Person, Class


@login_required(login_url='login')
def create_project(request):
    profile = request.user
    school_class = request.user.school_class

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.school_class = school_class
            project.save()
            return redirect('home', request.user.school_class.id)
    else:
        form = ProjectForm()
    return render(request, 'create_proj.html', {'form': form, 'profile': profile})


# Test view
# @login_required(login_url='login')
# def all_projects(request):
#     projects = Project.objects.all()
#     return render(request, 'all_proj.html', {'projects': projects})


@login_required(login_url='home')
def class_projects(request, pk):
    school_class = Class.objects.get(id=pk)
    projects = Project.objects.filter(school_class=school_class)
    profile = request.user

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.school_class = school_class
            project.save()
    else:
        form = ProjectForm()

    return render(request, 'projects/feed-post.html', {'projects': projects, 'class': school_class, 'profile': profile,
                                                       'form': form})


@login_required(login_url='home')
def single_project(request, pk):
    school_project = Project.objects.get(id=pk)
    return render(request, 'projects/project-page.html', {'project': school_project})


@login_required(login_url='login')
def comments(request):
    profile = request.user
    return render(request, 'projects/commentary.html', {'profile': profile})

