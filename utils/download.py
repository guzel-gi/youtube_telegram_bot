import os
from pydub import AudioSegment
from pytube import YouTube

def download_audio(url_link: str):
    yt = YouTube(url_link)
    streams = yt.streams
    title = yt.title
    file_name = f'{yt.video_id}.mp4'

    audio = streams.filter(only_audio=True, abr='128kbps', type='audio').desc().first()
    download_path = ".\\tmp"
    audio.download(output_path=download_path, filename=file_name)

    file_path = os.path.join(download_path, file_name)

    song = AudioSegment.from_file(file_path)
    file_name = f'{yt.video_id}.ogg'
    file_path = os.path.join(download_path, file_name)
    converted_song = song.export(file_path, format='ogg')
    
    info = {
        'file_path': file_path, 
        'title': title
        }
    return info

if __name__ == '__main__':
    r = download_audio('https://www.youtube.com/watch?v=rURichqTSvg')
    print(r)
    