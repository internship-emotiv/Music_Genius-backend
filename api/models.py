from django.db import models

class SpotifyPlaylist(models.Model):
    eng_spotify_id = models.CharField(max_length=100)
    exc_spotify_id = models.CharField(max_length=100)
    str_spotify_id = models.CharField(max_length=100)
    rel_spotify_id = models.CharField(max_length=100)
    int_spotify_id = models.CharField(max_length=100)
    foc_spotify_id = models.CharField(max_length=100)
    eng_playlist = models.CharField(max_length=100)
    exc_playlist = models.CharField(max_length=100)
    str_playlist = models.CharField(max_length=100)
    rel_playlist = models.CharField(max_length=100)
    int_playlist = models.CharField(max_length=100)
    foc_playlist = models.CharField(max_length=100)
