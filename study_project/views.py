from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout, get_user_model
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required, permission_required
from .forms import SignUpForm, ClassForm, PersonForm
from .models import Class, Person


def choose_group(request):
    groups = Group.objects.all()
    if request.method == 'POST':
        group_id = request.POST.get('group')
        group = Group.objects.get(id=group_id)
        request.session['group'] = group.name
        return redirect('pages')

    return render(request, 'study_project/home-page.html', {'groups': groups})


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            username = form.cleaned_data['username']
            name = form.cleaned_data['name']
            surname = form.cleaned_data['surname']
            image = form.cleaned_data['image']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = Person.objects.create_user(username=username,
                                              password=password,
                                              email=email,
                                              name=name,
                                              surname=surname,
                                              image=image)
            group = Group.objects.get(name=request.session.get('group'))
            group.user_set.add(user)
            user.save()
            if user is not None:
                login(request, user)
                return redirect('class')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'study_project/register-page.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if Person.objects.filter(school_class__isnull=True):
                login(request, user)
                return redirect('class')
            else:
                login(request, user)
                return redirect('home', request.user.school_class.id)
    return render(request, 'study_project/authorization-page.html')


def user_logout(request):
    logout(request)
    return redirect('login')


def pages_view(request):
    if request.session.get('group') == 'Student' or request.session.get('group') == 'Parent':
        return render(request, 'study_project/school-page.html')
    return render(request, 'study_project/teacher-page.html')


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('class')
    else:
        form = PersonForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': form})


@login_required(login_url='login')
def class_create(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            bio = form.cleaned_data['bio']
            if request.user.has_perms(['study_project.add_class', 'study_project.change_class']):
                school_class = Class.objects.create(name=name, bio=bio)
                school_class.save()
                Person.objects.update(school_class=school_class)
                return redirect('home', request.user.school_class.id)
            else:
                school_class = Class.objects.get(name=name)
                school_class.save()
                Person.objects.update(school_class=school_class)
                return redirect('home', request.user.school_class.id)
    else:
        form = ClassForm()
    return render(request, 'school_class.html', {'form': form})