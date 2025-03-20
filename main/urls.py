from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<str:username>/<int:id>/', views.post, name='post')
]