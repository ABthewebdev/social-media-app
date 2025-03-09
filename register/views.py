from django.shortcuts import render
from django.contrib.auth import login, authenticate
from .forms import CreateNewUser
from .models import CustomUser

def register(request):
    if request.method == "POST":
        form = CreateNewUser(request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = CustomUser.objects.create_user(username=u, password=p)
            user.save()
    else:
        form = CreateNewUser()

    return render(request, 'register/register.html', {"form":form})