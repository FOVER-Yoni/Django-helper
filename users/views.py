from django.shortcuts import render, HttpResponsePermanentRedirect, HttpResponse, redirect
from django.http import HttpResponse
from users.models import User
from users.forms import UserLoginForm
from django.contrib import auth
from django.urls import reverse
from users.forms import UserLoginForm, UserRegisterForm, UserProfileForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponsePermanentRedirect(reverse("index"))
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'users/login.html', context)
    

def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponsePermanentRedirect(reverse('users:login'))
    context = {'form': form}
    return render(request, 'users/register.html', context)


def profile(request):
    form = None
    if 'save' in request.POST:
        if request.method == "POST":
                form = UserProfileForm(instance=request.user, data=request.POST)
                if form.is_valid():
                    form.save()
                    return redirect('users:profile')



    if form is None:
        form = UserProfileForm(instance=request.user)



    user = User.objects.get(username=request.user)
    if 'send' in request.POST:
        if request.method == "POST":

            user.value = user.value + 1
            user.save()
            return redirect('users:profile')

    context = {'form': form, "label": user.value}
    return render(request, 'users/profile.html', context)
