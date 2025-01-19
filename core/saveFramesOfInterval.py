import argparse
import cv2
import os
import tempfile
from datetime import datetime, timedelta

def parse_time(time_str):
    return datetime.strptime(time_str, "%H:%M:%S")

def get_latest_video(videos_dir):
    files = [os.path.join(videos_dir, f) for f in os.listdir(videos_dir) if f.endswith(('.mp4', '.avi', '.mov'))]
    latest_file = max(files, key=os.path.getmtime)
    return latest_file

def save_frames(video_path, start_time, end_time, output_dir):
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Erro ao abrir o vídeo {video_path}")
        return
    
    fps = cap.get(cv2.CAP_PROP_FPS)
    start_frame = int(start_time.total_seconds() * fps)
    end_frame = int(end_time.total_seconds() * fps)
    
    cap.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
    
    frame_number = start_frame
    while frame_number <= end_frame:
        ret, frame = cap.read()
        if not ret:
            break
        frame_filename = os.path.join(output_dir, f"frame_{frame_number:06d}.png")
        cv2.imwrite(frame_filename, frame)
        frame_number += 1
    
    cap.release()

def main():
    parser = argparse.ArgumentParser(description="Extraia frames de um vídeo em um intervalo de tempo especificado e salve em uma subpasta temporária.\nDefault lasted video da pasta de video do windows")
    parser.add_argument('start_time', type=parse_time, help='Tempo inicial no formato hh:mm:ss')
    parser.add_argument('end_time', type=parse_time, help='Tempo final no formato hh:mm:ss')
    args = parser.parse_args()

    start_time = timedelta(hours=args.start_time.hour, minutes=args.start_time.minute, seconds=args.start_time.second)
    end_time = timedelta(hours=args.end_time.hour, minutes=args.end_time.minute, seconds=args.end_time.second)

    videos_dir = r'C:\Users\user\Videos'
    latest_video = get_latest_video(videos_dir)

    temp_dir = tempfile.gettempdir()
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    output_dir = os.path.join(temp_dir, f"yt_timestamp_{timestamp}")

    os.makedirs(output_dir, exist_ok=True)

    print(f"Salvando frames de {latest_video} entre {start_time} e {end_time} em {output_dir}")

    save_frames(latest_video, start_time, end_time, output_dir)

if __name__ == "__main__":
    main()
