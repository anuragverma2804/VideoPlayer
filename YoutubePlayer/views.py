from django.shortcuts import render
from django.shortcuts import render
from googleapiclient.discovery import build

def home(request):
    return render(request,'home.html')

def play_video(request):
    if request.method == 'POST':
        video_id = request.POST.get('video_id')  # Assuming video_id is passed via GET parameter
        api_key = 'AIzaSyDSp0mjzc77cQt4xjdzdH4OA2KCsDtKR4Y'
        youtube = build('youtube', 'v3', developerKey=api_key)
        video_response = youtube.videos().list(part='snippet', id=video_id).execute()
        video_details = video_response['items'][0] if video_response.get('items') else None
        print (video_details['snippet']['title'])
        return render(request, 'play_video.html', {'video_details': video_details})
    return render(request, 'play_video.html', {})

