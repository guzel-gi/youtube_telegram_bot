from pytube import YouTube, extract
from config import download_path

def download_video(url_link: str):                                       
    yt = YouTube(url_link)
    streams = yt.streams
    file_name = f'{yt.video_id}.ogg'

    audio = streams.filter(only_audio=True).desc().first()
    audio.download(output_path=download_path, filename=file_name)

    file_path = ''.join([download_path, file_name])
    return file_path


if __name__ == '__main__':
    print(download_video('https://www.youtube.com/watch?v=ZdEfKTTCyX4'))