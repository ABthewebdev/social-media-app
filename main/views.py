from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CreatePost
from register.models import CustomUser

# Create your views here.
def home(request):
    return render(request, 'main/home.html', {})

def create(request):
    if request.method == 'POST':
        form = CreatePost(request.POST)
        if form.is_valid():
            h = form.cleaned_data['headline']
            t = form.cleaned_data['text']
            p = Post(headline = h, text = t, author = request.user)
            p.save()
    else:
        form = CreatePost()
    return render(request, 'main/create.html', {"form": form})

def post(request, author, id):
    author = CustomUser.objects.get(username = author)
    post = author.post_set.get(id = id)
    context = {
        "post": post,
        "author": author
    }
    return render(request, 'main/post.html', context)

def profile(request, author):
    viewed_user = get_object_or_404(CustomUser, username = author)
    try:
        profile = CustomUser.objects.get(username = author)
    except CustomUser.DoesNotExist:
        profile = None
    if request.method == "POST":
        profile.followers += 1
        profile.save()
    return render(request, 'main/profile.html', {"profile": profile})