from pytube import YouTube

continuar = 'sim'

while continuar.lower() == 'sim':
    # URL do vídeo do YouTube
    video_url = input('Digite a URL do vídeo: ')

    yt = YouTube(video_url)

    video_title = yt.title

    # Melhor qualidade de áudio disponível
    stream = yt.streams.filter(only_audio=True, file_extension='mp4').first()

    audio_path = f'{video_title}.mp3'
    stream.download(output_path='', filename=f'{video_title}')

    print('Áudio baixado como MP3 com sucesso!')
    print(f'O título é: {video_title}')

    continuar = input("Deseja continuar (sim/não)? ")
