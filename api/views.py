from api.models import SpotifyPlaylist
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from api.serializers import UserSerializer, SpotifyPlaylistSerializer
from django.contrib.auth.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer

class SpotifyPlaylistViewSet(viewsets.ModelViewSet):
    queryset = SpotifyPlaylist.objects.all()
    serializer_class = SpotifyPlaylistSerializer
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]


