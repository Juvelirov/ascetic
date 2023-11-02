from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
from .models import Project
from study_project.models import Person


@login_required(login_url='login')
def create_project(request):
    profile = request.user.person
    #school_class = Person.objects.get(school_class=request.GET)

    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            #project.school_class = school_class
            project.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'create_proj.html', {'form': form, 'profile': profile})
