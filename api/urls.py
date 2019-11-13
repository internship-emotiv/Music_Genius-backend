from rest_framework import routers
from django.urls import path
from django.conf.urls import include
from .views import UserViewSet, SpotifyPlaylistViewSet


router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('spotifyplaylists', SpotifyPlaylistViewSet)

urlpatterns = [
    path('', include (router.urls)),
]