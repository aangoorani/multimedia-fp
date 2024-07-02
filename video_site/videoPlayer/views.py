from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .models import Video, Comment, Thumbnail
from django.urls import reverse


def index(request):
    return render(request, 'videoPlayer/index.html', {
        'thumbnails': Thumbnail.objects.all()
    })


def show(request, uri:str):
    encoded_uri = uri[:]
    uri = uri.replace("__", '/')

    if request.method == 'POST':
        res = submit_comment(request, uri)
        HttpResponseRedirect(reverse('video_page', args=(encoded_uri,)))

    # print(encoded_uri)

    # uri = urlsafe_base64_decode(uri).decode('utf-8')

    video = Video.objects.filter(uri=uri).first()
    # print(video)
    # Filter comments related to the specific video and order them by timestamp
    comments = Comment.objects.filter(video=video).order_by('-time_stamp')
    # print(comments)

    # Render the template with the video URI and comments
    if video.playback_type == 'local':
        return render(request, 'videoPlayer/video.html', {
            'uri': uri,
            'comments': comments,
            'encoded_uri': encoded_uri,
        })
    else:
        HttpResponse('Not implemented')


def submit_comment(request, uri: str):
    if request.method == 'POST':
        encoded_uri = uri[:]
        uri = uri.replace('__', '/')
        video = Video.objects.filter(uri=uri).first()
        name = request.POST.get('name')
        if not name: name = 'John Doe'
        text = request.POST.get('new_comment')
        print(request.POST)

        # Create a new Comment object and save it to the database
        comment = Comment(video=video, name=name, text=text, sentiment='default')
        comment.save()

        # Return a success response (could be a redirect or a JSON response)
        return JsonResponse({'message': 'Comment submitted successfully!'}, status=200)


