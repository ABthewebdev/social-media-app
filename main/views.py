from django.shortcuts import render
from .models import Post, Profile
from django.contrib.auth.models import User
from .forms import CreatePost

# Create your views here.
def home(request):
    users = User.objects.all()
    return render(request, 'main/home.html', {"users": users})

def profile(request, username):
    author = User.objects.get(username = username)
    profile = Profile.objects.get(user = author)
    context = {
        "profile": profile,
        "author": author
    }
    return render(request, 'main/profile.html', context)

def create(request):
    if request.method == "POST":
        form = CreatePost(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            post = Post(author = request.user, title = title, text = text)
            post.save()
    else:
        form = CreatePost()
    return render(request, 'main/create.html', {"form": form})

def post(request, username, id):
    author = User.objects.get(username = username)
    post = author.post_set.get(id = id)
    return render(request, 'main/post.html', {"post": post})