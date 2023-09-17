from pytube import YouTube
import os

class Baixar:
    def __init__(self, url):
        self.url = url

    def download(self):
        # URL do vídeo do YouTube
        video_url = self.url

        yt = YouTube(video_url)

        video_title = yt.title

        # Melhor qualidade de áudio disponível
        stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

                # Baixe o áudio em formato WAV
        audio_path = os.path.join('music', f'{video_title}.wav')
        stream.download(output_path='music/', filename=f'{video_title}.wav')