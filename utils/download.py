import os
from pytube import YouTube

def download_video(url_link: str):
    yt = YouTube(url_link)
    streams = yt.streams
    file_name = f'{yt.video_id}.ogg'
    title = yt.title

    audio = streams.filter(only_audio=True).desc().first()
    download_path = "/tmp"
    audio.download(output_path=download_path, filename=file_name)

    file_path = os.path.join(download_path, file_name)
    
    info = {
        'file_path': file_path, 
        'title': title
        }
    return info