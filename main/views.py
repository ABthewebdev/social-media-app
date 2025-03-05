from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CreatePost
from register.models import CustomUser

# Create your views here.
def home(response):
    return render(response, 'main/home.html', {})

def create(response):
    if response.method == 'POST':
        form = CreatePost(response.POST)
        if form.is_valid():
            h = form.cleaned_data['headline']
            t = form.cleaned_data['text']
            p = Post(headline = h, text = t, author = response.user)
            p.save()
            print(p.author)
    else:
        form = CreatePost()
    return render(response, 'main/create.html', {"form": form})

def post(response, author, id):
    author = CustomUser.objects.get(username = author)
    post = author.post_set.get(id = id)
    context = {
        "post": post,
        "author": author
    }
    return render(response, 'main/post.html', context)