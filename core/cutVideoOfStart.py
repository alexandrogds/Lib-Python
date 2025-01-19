
"""
corta o video mais recente da pasta de videos defaut no windows
recebe como entrada o tempo inicial e pega até o fim do video
e salva esse trecho excluindo assim o periodo inicial
"""

import argparse
import os
import glob
from datetime import datetime
from moviepy.editor import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

def get_most_recent_video(directory):
    list_of_files = glob.glob(os.path.join(directory, '*'))
    latest_file = max(list_of_files, key=os.path.getmtime)
    return latest_file

def parse_time(time_str):
    h, m, s = map(int, time_str.split(':'))
    return h * 3600 + m * 60 + s

def main():
    parser = argparse.ArgumentParser(description='Corta o vídeo mais recente na pasta especificada a partir do tempo inicial fornecido.')
    parser.add_argument('start_time', type=str, help='Tempo inicial no formato hh:mm:ss')
    args = parser.parse_args()

    start_time_seconds = parse_time(args.start_time)
    videos_directory = r'C:\Users\user\Videos'
    most_recent_video = get_most_recent_video(videos_directory)

    if not most_recent_video:
        print("Nenhum vídeo encontrado na pasta especificada.")
        return

    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    output_filename = os.path.join(videos_directory, f'cut_{timestamp}.mp4')

    # Obtendo a duração total do vídeo
    with VideoFileClip(most_recent_video) as video:
        duration = video.duration

    if start_time_seconds >= duration:
        print("O tempo inicial fornecido é maior que a duração do vídeo.")
        return

    # Definindo o tempo final como a duração do vídeo
    end_time_seconds = duration

    # Cortando o vídeo
    ffmpeg_extract_subclip(most_recent_video, start_time_seconds, end_time_seconds, targetname=output_filename)
    print(f"Vídeo cortado salvo como {output_filename}")

if __name__ == "__main__":
    main()
