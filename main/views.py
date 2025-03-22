from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from .models import Post, Profile, Message
from django.contrib.auth.models import User
from .forms import CreatePost, CreateMessage

# Create your views here.
def home(request):
    users = User.objects.all()
    posts = Post.objects.all()
    context = {
        "users": users,
        "posts": posts
    }
    return render(request, 'main/home.html', context)

def profile(request, username):
    author = User.objects.get(username = username)
    profile = Profile.objects.get(user = author)
    is_following = profile.is_followed_by(request.user)
    context = {
        "profile": profile,
        "is_following": is_following,
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
    author = User.objects.get_object_or_404(username = username)
    post = author.post_set.get(id = id)
    return render(request, 'main/post.html', {"post": post})


def follow_toggle(request, profile_id):
    if request.method == 'POST':
        profile = get_object_or_404(Profile, id=profile_id)
        
        # Don't allow users to follow themselves
        if request.user == profile.user:
            return JsonResponse({'status': 'error', 'message': 'You cannot follow yourself'})
        
        # Toggle follow status
        if profile.is_followed_by(request.user):
            profile.followers.remove(request.user)
            is_following = False
        else:
            profile.followers.add(request.user)
            is_following = True
            
        return JsonResponse({
            'status': 'success',
            'is_following': is_following,
            'followers_count': profile.get_followers_count()
        })
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})


def direct_messages(request, username):
    users = User.objects.all()
    user2 = User.objects.get(username=username)
    
    # Get messages from both directions
    my_messages = Message.objects.filter(sender=request.user, receiver=user2)
    their_messages = Message.objects.filter(sender=user2, receiver=request.user)
    
    # Combine the querysets and order by timestamp
    all_messages = my_messages.union(their_messages).order_by('timestamp')
    # Use 'timestamp' or whatever field you use to track when messages were sent

    profile = Profile.objects.get(user = user2)
    
    if request.method == "POST":
        form = CreateMessage(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            message = Message(receiver=user2, text=text, sender=request.user)
            message.save()
            return HttpResponseRedirect('/messages/%s' %username)  # Redirect to refresh
    else:
        form = CreateMessage()
    
    context = {
        "user2": user2,
        "users": users,
        "all_messages": all_messages,
        "profile": profile,
        "form": form
    }
    
    return render(request, 'main/message.html', context)

def settings(request):
    return render(request, 'main/settings.html', {})