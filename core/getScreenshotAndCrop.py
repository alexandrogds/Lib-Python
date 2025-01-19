import os
import argparse
import pyautogui
from PIL import Image
from datetime import datetime

def crop_image(input_path, output_path, x1, y1, x2, y2):
    with Image.open(input_path) as img:
        cropped_img = img.crop((x1, y1, x2, y2))
        cropped_img.save(output_path)

def main():
    parser = argparse.ArgumentParser(description="Corta uma screenshot.")
    parser.add_argument("--output_path", type=str, default=r"C:\Users\user\OneDrive\images\Screenshots\tyrania", help="Caminho para a pasta onde a imagem cortada será salva. O padrão é 'C:\\Users\\user\\OneDrive\\images\\Screenshots\tyrania'.")
    parser.add_argument("--x1", type=int, default=45, help="Coordenada X do canto superior esquerdo do corte.")
    parser.add_argument("--y1", type=int, default=591, help="Coordenada Y do canto superior esquerdo do corte.")
    parser.add_argument("--x2", type=int, default=1301, help="Coordenada X do canto inferior direito do corte.")
    parser.add_argument("--y2", type=int, default=747, help="Coordenada Y do canto inferior direito do corte.")
    
    args = parser.parse_args()
    
    # Capturar a screenshot
    screenshot = pyautogui.screenshot()
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_filename = f"screenshot_{timestamp}.png"
    screenshot_path = os.path.join(args.output_path, screenshot_filename)
    screenshot.save(screenshot_path)
    
    # Calcular width e height
    width = args.x2 - args.x1
    height = args.y2 - args.y1
    
    # Cortar a imagem
    output_filename = f"cropped_{timestamp}.png"
    output_path = os.path.join(args.output_path, output_filename)
    crop_image(screenshot_path, output_path, args.x1, args.y1, args.x2, args.y2)
    print(f"Imagem cortada salva em: {output_path}")

if __name__ == "__main__":
    main()
