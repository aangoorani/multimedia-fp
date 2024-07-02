from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Video, Comment, Thumbnail
from django.urls import reverse
from .utils.aiAgent import comment_analyzer, summary_generator

def index(request):
    return render(request, 'videoPlayer/index.html', {
        'thumbnails': Thumbnail.objects.all()
    })


def show(request, uri: str):
    encoded_uri = uri[:]
    uri = uri.replace("__", '/')

    if request.method == 'POST':
        return submit_comment(request, uri)

    video = Video.objects.filter(uri=uri).first()

    # Filter comments related to the specific video and order them by timestamp
    comments = Comment.objects.filter(video=video).order_by('-time_stamp')

    # Render the template with the video URI and comments
    context = {
        'uri': uri,
        'comments': comments,
        'encoded_uri': encoded_uri,
    }
    if video.playback_type == 'local':
        return render(request, 'videoPlayer/video.html', context)
    elif video.playback_type == 'dash':
        return render(request, 'videoPlayer/dash_video.html', context)
    elif video.playback_type == 'cdn1':
        return render(request, 'videoPlayer/cdn_dash.html', context)
    elif video.playback_type == 'cdn2':
        return render(request, 'videoPlayer/cdn_hls.html', context)
    else:
        return HttpResponse("NOT Implemented")

def submit_comment(request, uri: str):
    if request.method == 'POST':
        uri = uri.replace('__', '/')
        video = Video.objects.filter(uri=uri).first()
        name = request.POST.get('name')
        if not name:
            name = 'John Doe'
        text = request.POST.get('new_comment')

        # Create a new Comment object and save it to the database
        comment = Comment(video=video, name=name, text=text, sentiment='default')
        sentiment = comment_analyzer.analyze(text)
        comment.sentiment = sentiment
        comment.save()

        # Return a success response (JSON response)
        return JsonResponse({'message': 'Comment submitted successfully!'}, status=200)


# for requesting to generate summary, uncomment when needed, also uncomment the relevant path in urls.py
# def extra(request):
#     thumbnails = Thumbnail.objects.all()
#     i=0
#     for thumbnail in thumbnails:
#         print(thumbnail)
#         yt_link = thumbnail.video.yt_link
#         summary = summary_generator.summarize_youtube_video(yt_link)
#         thumbnail.summary = summary
#         thumbnail.save(update_fields=['summary'])
#         i+=1
#         print('done:', i)
#
#     return HttpResponse('Done')
