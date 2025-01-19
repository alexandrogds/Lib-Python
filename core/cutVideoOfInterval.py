import os
import argparse
from moviepy.editor import VideoFileClip
from datetime import datetime

def get_last_modified_video(folder_path):
    """
    Retorna o caminho do último vídeo modificado em uma pasta.
    """
    videos = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith(('.mp4', '.avi', '.mkv'))]
    if not videos:
        return None
    return max(videos, key=os.path.getmtime)

def parse_time(time_str):
    """
    Converte uma string de tempo no formato hh:mm:ss para segundos.
    """
    parts = time_str.split(':')
    hours = int(parts[0])
    minutes = int(parts[1])
    seconds = int(parts[2])
    total_seconds = hours * 3600 + minutes * 60 + seconds
    return total_seconds

def cut_video(video_path, folder_output_path, time_start, time_end):
    """
    Corta o vídeo de acordo com os tempos especificados.
    """
    output_filename = os.path.join(folder_output_path, os.path.basename(video_path))
    clip = VideoFileClip(video_path)
    clip = clip.subclip(parse_time(time_start), parse_time(time_end))
    clip.write_videofile(output_filename)
    clip.close()

def main():
    parser = argparse.ArgumentParser(description='Script para cortar vídeos.')
    parser.add_argument('video_path', nargs='?', default=get_last_modified_video(r'C:\Users\user\Videos\\'),
                        help='Caminho do vídeo a ser cortado (padrão: último vídeo modificado na pasta "C:\\Users\\user\\Videos\\")')
    parser.add_argument('--folder_output_path', default=r'C:\Users\user\Videos\yt\\',
                        help='Caminho da pasta de saída para o vídeo cortado (padrão: "C:\\Users\\user\\Videos\\yt\\")')
    parser.add_argument('--time_start', required=True, help='Tempo de início do corte no formato hh:mm:ss')
    parser.add_argument('--time_end', required=True, help='Tempo de fim do corte no formato hh:mm:ss')
    args = parser.parse_args()

    cut_video(args.video_path, args.folder_output_path, args.time_start, args.time_end)

if __name__ == "__main__":
    main()
