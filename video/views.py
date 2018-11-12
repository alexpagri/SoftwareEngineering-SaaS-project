from django.shortcuts import render
from video.models import VideoModel

# Create your views here.

def video_detail(request, vid_id):
    return render(request, 'video_details.html', {'details':VideoModel.objects.get(id = vid_id).details})

def video(request):
    return render(request, 'videos.html', {'vids':VideoModel.objects.order_by('title')})
