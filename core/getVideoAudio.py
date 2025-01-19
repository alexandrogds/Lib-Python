import argparse
from moviepy.editor import VideoFileClip

def extrair_audio(video_path, audio_path):
    """Extrai o áudio de um arquivo de vídeo e salva em um arquivo de áudio."""
    video_clip = VideoFileClip(video_path)
    audio_clip = video_clip.audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    video_clip.close()

def main():
    parser = argparse.ArgumentParser(
        description="Extrai o áudio de um arquivo de vídeo e salva em um arquivo de áudio."
    )
    
    parser.add_argument(
        "video_path",
        type=str,
        help="O caminho para o arquivo de vídeo de onde o áudio será extraído."
    )
    
    parser.add_argument(
        "audio_path",
        type=str,
        help="O caminho para o arquivo de áudio onde o áudio extraído será salvo."
    )
    
    args = parser.parse_args()
    
    extrair_audio(args.video_path, args.audio_path)
    print(f"Áudio extraído com sucesso e salvo em {args.audio_path}")

if __name__ == "__main__":
    main()
