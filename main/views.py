from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import Post
from .forms import CreatePost
from register.models import CustomUser
from .models import Follower
from django.contrib.auth.decorators import login_required


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
    profile = CustomUser.objects.get(username = author)
    if request.method == "POST":
        if 'follow-button' in request:
            profile.followers += 1
            profile.save()
        elif 'unfollow-button' in request:
            profile.followers -= 1
            profile.save()
    context = {
        "profile":profile
    }
    return render(request, 'main/profile.html', context)

@login_required
def toggle_follow(request, author):
    followed_user = get_object_or_404(CustomUser, username=author)
    
    if request.user == followed_user:
        return JsonResponse({"error": "You cannot follow yourself"}, status=400)
    
    follow_relation, created = Follower.objects.get_or_create(
        follower=request.user, 
        followed=followed_user
    )

    if not created:
        follow_relation.delete()  # If already following, unfollow
        return JsonResponse({"message": "Unfollowed"})
    
    return JsonResponse({"message": "Followed"})
