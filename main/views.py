from django.shortcuts import render
from .models import Post, Profile

# Create your views here.
def home(request):
    return render(request, 'main/home.html', {})
