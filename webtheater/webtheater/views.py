from django.shortcuts import render, redirect
from webtheater.models.video import Video

video_list = [
    Video(1, "https://www.youtube.com/embed/waTob1IM4UM",
        "thor.png", 
        "Thor: Love and Thunder | Official Teaser", 
        "Here it is. ❤️  + ⚡", 
        7923794, 
        "916 Mil", 
        "18 de abril de 2022"
        ),
    Video(2, "https://www.youtube.com/embed/m9EX0f6V11Y",
        "ms_marvel.jpg",
        "Marvel Studios Ms. Marvel | Official Trailer | Disney+", 
        "The future is in her hands.", 
        17655417,
        "733 Mil",
        "15 de março de 2022"
        )
]

def index(request):
    return render(request, "index.html", {"video_list":video_list})

def ver_video(request, id:int):
    for video in video_list:
        if id == video.get_id():
            return render(request, "video.html", {"video":video})