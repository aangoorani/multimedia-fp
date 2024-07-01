from ..models import Thumbnail, Video


def generate_thumbnail(videos, num=6):
    thumbnails = []
    for _ in range(num):
        thumbnails.append(Thumbnail())

    for i in range(num):
        if i == 0:
            thumbnails[i].video = videos[i]
            thumbnails[i].duration = 4 * 60 + 34
            thumbnails[i].title = "Monster Jerry"
            thumbnails[i].image = 'videoPlayer/thumbnails/thumbnail1.jpeg'
        elif i == 1:
            thumbnails[i].video = videos[i]
            thumbnails[i].duration = 4 * 60 + 39
            thumbnails[i].title = "Taking Care Of Tom"
            thumbnails[i].image = 'videoPlayer/thumbnails/thumbnail2.jpeg'
        elif i == 2:
            thumbnails[i].video = videos[i]
            thumbnails[i].duration = 5 * 60 + 56
            thumbnails[i].title = "Ball Tom"
            thumbnails[i].image = 'videoPlayer/thumbnails/thumbnail3.jpeg'
        elif i == 3:
            thumbnails[i].video = videos[i]
            thumbnails[i].duration = 7 * 60 + 16
            thumbnails[i].title = "Fake Kangaroo Tom"
            thumbnails[i].image = 'videoPlayer/thumbnails/thumbnail4.jpeg'
        elif i == 4:
            pass
        else:
            pass
    return thumbnails


def generate_video(num=6):
    videos = []
    for _ in range(num):
        videos.append(Video())

    for i in range(num):
        if i == 0:
            videos[i].uri = 'videoPlayer/video_files/video_files/vid1.mp4'
            videos[i].playback_type = 'local'
        elif i == 1:
            videos[i].uri = 'videoPlayer/video_files/vid2.mp4'
            videos[i].playback_type = 'local'
        elif i == 2:
            videos[i].uri = 'videoPlayer/video_files/vid3.mp4'
            videos[i].playback_type = 'dash'
        elif i == 3:
            videos[i].uri = 'videoPlayer/video_files/vid4.mp4'
            videos[i].playback_type = 'dash'
        elif i == 4:
            pass
        else:
            pass
    return videos

