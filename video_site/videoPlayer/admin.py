from django.contrib import admin
from .models import Video, Thumbnail, Comment

# Register your models here.

admin.site.register(Video)
admin.site.register(Comment)
admin.site.register(Thumbnail)
