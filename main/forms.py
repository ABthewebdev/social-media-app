from django import forms
from .models import Post, Message

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'imageSrc']

class CreateMessage(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['text']