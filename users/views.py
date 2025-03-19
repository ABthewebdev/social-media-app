from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from main.models import Profile

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile(user = user)
            profile.save()

    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {"form": form})
