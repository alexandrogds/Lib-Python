
"""
"""
import argparse
from PIL import Image

def crop_image(input_path, output_path, x, y, width, height):
    with Image.open(input_path) as img:
        cropped_img = img.crop((x, y, x + width, y + height))
        cropped_img.save(output_path)

def main():
    parser = argparse.ArgumentParser(description="Corta uma imagem.")
    parser.add_argument("input_path", help="Caminho para a imagem de entrada.")
    parser.add_argument("output_path", help="Caminho para a imagem de saída.")
    parser.add_argument("x", type=int, help="Coordenada X do canto superior esquerdo do corte.")
    parser.add_argument("y", type=int, help="Coordenada Y do canto superior esquerdo do corte.")
    parser.add_argument("width", type=int, help="Largura do corte.")
    parser.add_argument("height", type=int, help="Altura do corte.")

    args = parser.parse_args()

    crop_image(args.input_path, args.output_path, args.x, args.y, args.width, args.height)

if __name__ == "__main__":
    main()
