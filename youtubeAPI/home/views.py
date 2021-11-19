from django.shortcuts import render
from django.conf import settings

from datetime import datetime, timezone
import requests


def search_results(request):
    videos = []
    query = ""
    if request.method=='POST':  #if method is post then sending GET request to the Youtube Data API
        query = request.POST['query']
        params = {
            'part': 'snippet',
            'q': query,
            'order': 'date',
            'publishedBefore': datetime.now(timezone.utc).isoformat('T'),
            'type': 'video',
            'maxResults': 9,
            'key': settings.YOUTUBE_DATA_KEY
        }
        endpoint = "https://www.googleapis.com/youtube/v3/search"
        responses = requests.get(endpoint, params=params).json()['items']
        

        for response in responses:
            video_data = {
                'title' : response['snippet']['title'],
                'id' : response['id'],
                'url' : f'https://www.youtube.com/watch?v={response["id"]}',
                'thumbnail' : response['snippet']['thumbnails']['high']['url']
            }
            videos.append(video_data)

    return render(request, 'home/index.html', {'videos': videos, 'query':query})