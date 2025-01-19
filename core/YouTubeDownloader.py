import argparse
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, url, output_path):
        self.url = url
        self.output_path = output_path

    def download_video(self):
        try:
            yt = YouTube(self.url)
            print(f"Baixando: {yt.title}")

            # Seleciona a maior resolução disponível
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=self.output_path)
            
            print(f"Download concluído! Vídeo salvo em: {self.output_path}")
        
        except Exception as e:
            print(f"Ocorreu um erro: {e}")

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Script para baixar vídeos do YouTube."
    )

    parser.add_argument(
        'url', 
        type=str, 
        help="URL do vídeo do YouTube."
    )

    parser.add_argument(
        'output_path', 
        type=str, 
        help="Caminho da pasta onde o vídeo será salvo."
    )

    return parser.parse_args()

def main():
    args = parse_arguments()
    downloader = YouTubeDownloader(args.url, args.output_path)
    downloader.download_video()

if __name__ == "__main__":
    main()
