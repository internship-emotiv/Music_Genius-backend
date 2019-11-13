from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpotifyPlaylist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eng_spotify_id', models.CharField(max_length=100)),
                ('exc_spotify_id', models.CharField(max_length=100)),
                ('str_spotify_id', models.CharField(max_length=100)),
                ('rel_spotify_id', models.CharField(max_length=100)),
                ('int_spotify_id', models.CharField(max_length=100)),
                ('foc_spotify_id', models.CharField(max_length=100)),
                ('eng_playlist', models.CharField(max_length=100)),
                ('exc_playlist', models.CharField(max_length=100)),
                ('str_playlist', models.CharField(max_length=100)),
                ('rel_playlist', models.CharField(max_length=100)),
                ('int_playlist', models.CharField(max_length=100)),
                ('foc_playlist', models.CharField(max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
