from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .models import UserProfile


def dashboard(request):
    return render(request, 'users/dashboard.html')


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": UserCreationForm}
        )
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            user_profile = UserProfile(user=user)
            user_profile.save()
            return redirect(reverse("dashboard"))
