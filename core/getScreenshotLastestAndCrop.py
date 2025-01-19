
"""
"""

import os
import argparse
from PIL import Image
from datetime import datetime

class RecentImageFinder:
    def __init__(self, folder_path):
        self.folder_path = folder_path

    def get_most_recent_image(self):
        files = [os.path.join(self.folder_path, f) for f in os.listdir(self.folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
        if not files:
            raise FileNotFoundError("Nenhuma imagem encontrada na pasta especificada.")
        most_recent_file = max(files, key=os.path.getmtime)
        return most_recent_file

def crop_image(input_path, output_path, x1, y1, x2, y2, x3, y3, x4, y4):
    with Image.open(input_path) as img:
        cropped_img = img.crop((x1, y1, x2, y2, x3, y3, x4, y4))
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f"{timestamp}.jpg"
        output_path = os.path.join(output_path, output_filename)
        cropped_img.save(output_path)

def main():
    parser = argparse.ArgumentParser(description="Corta uma imagem.")
    parser.add_argument("--output_path", type=str, default=r"C:\Users\user\OneDrive\images\Screenshots", help="Caminho para a pasta onde a imagem cortada será salva. O padrão é 'C:\Users\user\OneDrive\images\Screenshots'.")
    parser.add_argument("--x1", type=int, default=45, help="Coordenada X do canto superior esquerdo do corte.")
    parser.add_argument("--y1", type=int, default=591, help="Coordenada Y do canto superior esquerdo do corte.")
    parser.add_argument("--x2", type=int, default=1301, help="Coordenada X do canto superior direito do corte.")
    parser.add_argument("--y2", type=int, default=592, help="Coordenada Y do canto superior direito do corte.")
    parser.add_argument("--x3", type=int, default=29, help="Coordenada X do canto inferior esquerdo do corte.")
    parser.add_argument("--y3", type=int, default=740, help="Coordenada Y do canto inferior esquerdo do corte.")
    parser.add_argument("--x4", type=int, default=1338, help="Coordenada X do canto inferior direito do corte.")
    parser.add_argument("--y4", type=int, default=747, help="Coordenada Y do canto inferior direito do corte.")
    
    args = parser.parse_args()
    
    # Encontrar a imagem mais recente na pasta especificada
    folder_path = r"C:\Users\user\OneDrive\images\Screenshots"
    finder = RecentImageFinder(folder_path)
    input_path = finder.get_most_recent_image()
    
    # Cortar a imagem
    crop_image(input_path, args.output_path, args.x1, args.y1, args.x2, args.y2, args.x3, args.y3, args.x4, args.y4)
    print(f"Imagem cortada salva em: {args.output_path}")

if __name__ == "__main__":
    main()
