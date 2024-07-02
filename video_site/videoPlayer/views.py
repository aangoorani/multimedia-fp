from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Video, Comment, Thumbnail
from django.urls import reverse


def index(request):
    return render(request, 'videoPlayer/index.html', {
        'thumbnails': Thumbnail.objects.all()
    })

#
# def show(request, uri:str):
#     encoded_uri = uri[:]
#     uri = uri.replace("__", '/')
#
#     if request.method == 'POST':
#         submit_comment(request, uri)
#         # HttpResponseRedirect(reverse('video_page', args=(encoded_uri,)))
#
#     video = Video.objects.filter(uri=uri).first()
#
#     # Filter comments related to the specific video and order them by timestamp
#     comments = Comment.objects.filter(video=video).order_by('-time_stamp')
#     # print(comments)
#
#     # Render the template with the video URI and comments
#     if video.playback_type == 'local':
#         return render(request, 'videoPlayer/video.html', {
#             'uri': uri,
#             'comments': comments,
#             'encoded_uri': encoded_uri,
#         })
#
#     elif video.playback_type == 'dash':
#         return render(request, 'videoPlayer/dash_video.html', {
#             'uri': uri,
#             'comments': comments,
#             'encoded_uri': encoded_uri,
#         })
#     elif video.playback_type == 'cdn1':
#         return render(request, 'videoPlayer/cdn_dash.html', {
#             'uri': uri,
#             'comments': comments,
#             'encoded_uri': encoded_uri,
#         })
#     elif video.playback_type == 'cdn2':
#         return render(request, 'videoPlayer/cdn_hls.html', {
#             'uri': uri,
#             'comments': comments,
#             'encoded_uri': encoded_uri,
#         })
#     else:
#         return HttpResponse("NOT Implemented")
#
# def submit_comment(request, uri: str):
#     if request.method == 'POST':
#         encoded_uri = uri[:]
#         uri = uri.replace('__', '/')
#         video = Video.objects.filter(uri=uri).first()
#         name = request.POST.get('name')
#         if not name: name = 'John Doe'
#         text = request.POST.get('new_comment')
#         print(request.POST)
#
#         # Create a new Comment object and save it to the database
#         comment = Comment(video=video, name=name, text=text, sentiment='default')
#         comment.save()
#
#         # Return a success response (could be a redirect or a JSON response)
#         return JsonResponse({'message': 'Comment submitted successfully!'}, status=200)



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
        comment.save()

        # Return a success response (JSON response)
        return JsonResponse({'message': 'Comment submitted successfully!'}, status=200)