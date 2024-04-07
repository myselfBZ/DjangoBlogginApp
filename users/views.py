from django.shortcuts import render, redirect 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from .forms import ProfileForm
from .models import Profile
def register(request:HttpRequest):
    form = UserCreationForm()
    if request.user.is_authenticated:
        return redirect("posts/")
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.create(user=user, bio="No information.")
            login(request, user)
            return redirect('/posts/')
    return render(request, 'register.html', {"form":form})

@login_required
def log_out(request):
    logout(request)
    return redirect('/login/')


@login_required
def see_profile(request, username):
    user = User.objects.get(username=username)
    form = ProfileForm(instance=user.profile)
    return render(request, 'profile.html', {"owner":user, "form":form})

@login_required
def update_profile(request):
    user = request.user
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=user.profile)
        if form.is_valid():
            form.save()
            return redirect(f"http://127.0.0.1:8000/profile/{user.username}")
        else:
            print(form.errors)
   