from django.utils.http import urlsafe_base64_encode
from django.db import models
import json

# Create your models here.
class Video(models.Model):
    playback_values = [
        ('local', 'local'),
        ('dash', 'dash'),
        ('cdn1', 'cdn_dash'),
        ('cdn2', 'cdn_hls')
    ]

    playback_type = models.CharField(max_length=10, choices=playback_values)
    uri = models.CharField(max_length=200, default='N/A', unique=True)
    yt_link = models.URLField(max_length=200, default='N/A')

    def __str__(self):
        d = {'playback type': self.playback_type, 'location': self.uri, 'youtube': self.yt_link}
        return json.dumps(d)

    def get_id(self):
        s = str(self.uri).replace('/', '__')
        # s = bytes(str(self.uri))
        # s = urlsafe_base64_encode(s).encode('utf-8')
        return s

class Thumbnail(models.Model):
    title = models.CharField(max_length=100, default='Tom and Jerry')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='thumbnail')
    duration = models.IntegerField(help_text="video duration in seconds")
    genre = models.CharField(max_length=50, default='comedy')
    year = models.IntegerField(default=2000)
    image = models.CharField(max_length=200)
    summary = models.CharField(max_length=200, default="No summary available at the moment")

    def __str__(self):
        d = {'title': self.title, 'genre': self.genre, 'year': self.year, 'image': self.image, 'video name': self.video.uri}
        return json.dumps(d)

    def get_text(self):
        m , s = divmod(self.duration, 60)
        return f'''<strong>{self.title}</strong><br>{self.year} {self.genre} {m}:{s}<br>{self.summary}<br>playback: {self.video.playback_type}'''


class Comment(models.Model):
    sentiment_values = [
        ('positive', 'positive'),
        ('negative', 'negative'),
        ('neutral', 'neutral'),
        ('default', 'default'),
    ]

    sentiment = models.CharField(max_length=20, choices=sentiment_values, default='default')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30, default='John Doe')
    text = models.CharField(max_length=300, default='great video!!!')
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        happy_face = "\U0001F600"
        sad_face = "\U0001F641"
        neutral_face = "\U0001F610"
        ok = "\U0001F44C"
        face = {'positive': happy_face, 'negative': sad_face, 'neutral': neutral_face, 'default': ok}
        return f"{self.name} {face[self.sentiment]}:\n{self.text}"

    def get_text(self):
        return self.__str__()
