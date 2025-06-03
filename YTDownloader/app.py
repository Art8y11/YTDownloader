import yt_dlp
import os
from colorama import init, Fore

init(autoreset=True)

ffmpeg_path = os.path.join(os.getcwd(), 'ffmpeg.exe')

print(Fore.CYAN + '📥 Cole o link do vídeo do Youtube:')
link = input()

print(Fore.YELLOW + '🎵 Escolha o formato (mp3/mp4):')
formato = input().strip().lower()

pasta_download = 'downloads'
os.makedirs(pasta_download, exist_ok=True)

ydl_opts = {}

if formato == 'mp3':
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(pasta_download, '%(title)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': ffmpeg_path,
        'noplaylist': True,
    }
elif formato == 'mp4':
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(pasta_download, '%(title)s.%(ext)s'),
        'merge_output_format': 'mp4',
        'ffmpeg_location': ffmpeg_path,
        'noplaylist': True,
    }
else:
    print(Fore.RED + '❌ Formato inválido. Escolha "mp3" ou "mp4".')
    exit()

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([link])

print(Fore.GREEN + '✅ Download concluído com sucesso!')
