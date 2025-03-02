from django.shortcuts import render
from .models import Post
from .forms import CreatePost
from register.models import CustomUser

# Create your views here.
def home(response):
    if not CustomUser.objects.filter(id=id).exists():
        print("Invalid user ID:", id)

    return render(response, 'main/home.html', {})

def create(response):
    if response.method == 'POST':
        form = CreatePost(response.POST)
        if form.is_valid():
            h = form.cleaned_data['headline']
            t = form.cleaned_data['text']
            p = Post.objects.create(headline = h, text = t)
            p.save()
    else:
        form = CreatePost()
    return render(response, 'main/create.html', {"form": form})