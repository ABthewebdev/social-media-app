from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('settings/', views.settings, name='settings'),
    path('create/', views.create, name='create'),
    path('profile/<str:username>/', views.profile, name='profile'),
    path('<str:username>/<int:id>/', views.post, name='post'),
    path('profile/follow/<int:profile_id>/', views.follow_toggle, name='follow_toggle'),
    path('messages/', views.messages, name="messages"),
    path('messages/<str:username>/', views.direct_messages, name='direct_messages')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)