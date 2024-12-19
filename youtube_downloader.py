import os
import yt_dlp

def download_video(video_url, save_path):
    ydl_opts = {
        'format': 'best[ext=mp4]/best',
        'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s'),
        'noplaylist': True,  # Baixa apenas um vídeo, mesmo se o link for de uma playlist
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([video_url])
        print("Download concluído!")
    except Exception as e:
        print(f"Erro ao baixar o vídeo: {e}")

if __name__ == "__main__":
    video_url = input("Insira o link do vídeo do YouTube: ")
    save_path = "downloads"
    os.makedirs(save_path, exist_ok=True)
    download_video(video_url, save_path)
