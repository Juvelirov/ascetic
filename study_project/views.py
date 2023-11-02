from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, ClassForm, PersonForm
from .models import Class, Person


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            user = User.objects.create_user(username=username, password=password, email=email)
            groups = form.cleaned_data['group']
            for group_name in groups:
                group = Group.objects.get(name=group_name)
                group.user_set.add(user)
            user.save()
            if user is not None:
                login(request, user)
                return redirect('edit_profile')
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('class')
    return render(request, 'login.html')


def user_logout(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def edit_profile(request):
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=request.user.person)
        if form.is_valid():
            form.save()
            return redirect('class')
    else:
        form = PersonForm(instance=request.user.person)
    return render(request, 'edit_profile.html', {'form': form})


@login_required(login_url='login')
def class_autorize(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            bio = form.cleaned_data['bio']
            school_class = Class.objects.create(name=name, bio=bio)
            school_class.save()
            Person.objects.update(school_class=school_class)
            return redirect('home')
    else:
        form = ClassForm()
    return render(request, 'school_class.html', {'form': form})