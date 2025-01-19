import argparse
import cv2
import numpy as np
import os
from datetime import datetime

def get_most_recent_image(directory):
    files = [os.path.join(directory, f) for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
    return files[0] if files else None

def create_video(image_path, duration, output_path):
    # Duração em segundos
    h, m, s = map(int, duration.split(':'))
    total_seconds = h * 3600 + m * 60 + s
    
    # Carregar a imagem
    image = cv2.imread(image_path)
    height, width, layers = image.shape
    
    # Definir parâmetros do vídeo
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = 30
    video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    # Calcular o número de frames
    num_frames = total_seconds * fps
    
    # Adicionar frames ao vídeo
    for _ in range(num_frames):
        video.write(image)
    
    # Finalizar o vídeo
    video.release()
    print(f"Vídeo criado em {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Cria um vídeo de uma imagem com duração especificada.")
    
    # Argumentos
    parser.add_argument('duration', type=str, help='Duração do vídeo no formato hh:mm:ss')
    
    parser.add_argument(
        '--image', type=str, default=get_most_recent_image(r'C:\Users\user\OneDrive\images\Screenshots\tyrania\thumbnail'),
        help='Caminho da imagem a ser utilizada. (Default: imagem mais recente da pasta C:\\Users\\user\\OneDrive\\images\\Screenshots\\tyrania\\thumbnail\\)'
    )
    
    parser.add_argument(
        '--outpath', type=str, default=r'C:\Users\user\Videos\yt\output_video.mp4',
        help='Caminho de saída do vídeo a ser criado. (Default: C:\\Users\\user\\Videos\\yt\\)'
    )
    
    args = parser.parse_args()
    
    # Criar o vídeo
    create_video(args.image, args.duration, args.outpath)

if __name__ == '__main__':
    main()
