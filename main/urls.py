from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('<str:author>/', views.profile, name='profile'),
    path('<str:author>/<int:id>/', views.post, name='post')
]