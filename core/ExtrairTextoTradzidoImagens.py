import fitz
import os
import argparse
from googletrans import Translator

class PDFExtractor:
    def __init__(self, input_file, output_folder):
        self.input_file = input_file
        self.output_folder = output_folder
        self.translator = Translator()

    def extract_text_and_images(self):
        try:
            # Verifica se o arquivo de entrada existe
            if not os.path.exists(self.input_file):
                raise FileNotFoundError(f"Arquivo não encontrado: {self.input_file}")

            # Cria a pasta de saída se não existir
            if not os.path.exists(self.output_folder):
                os.makedirs(self.output_folder)

            # Abre o arquivo PDF
            doc = fitz.open(self.input_file)
            text_output = os.path.join(self.output_folder, "extracted_text.txt")
            translated_text_output = os.path.join(self.output_folder, "translated_text.txt")

            with open(text_output, "w", encoding="utf-8") as text_file, \
                 open(translated_text_output, "w", encoding="utf-8") as translated_text_file:
                
                for page_num in range(len(doc)):
                    page = doc.load_page(page_num)
                    text = page.get_text()
                    text_file.write(f"----- Página {page_num + 1} -----\n")
                    text_file.write(text + "\n")

                    # Tradução do texto
                    translated_text = self.translator.translate(text, src='auto', dest='pt').text
                    translated_text_file.write(f"----- Página {page_num + 1} -----\n")
                    translated_text_file.write(translated_text + "\n")

                    image_list = page.get_images(full=True)
                    for img_index, img in enumerate(image_list):
                        xref = img[0]
                        base_image = doc.extract_image(xref)
                        image_bytes = base_image["image"]
                        image_ext = base_image["ext"]
                        image_filename = os.path.join(self.output_folder, f"image_page{page_num + 1}_{img_index + 1}.{image_ext}")

                        with open(image_filename, "wb") as img_file:
                            img_file.write(image_bytes)

            print(f"Texto e imagens extraídos e traduzidos com sucesso para a pasta: {self.output_folder}")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Script para extrair e traduzir texto e imagens de um PDF em ordem."
    )

    parser.add_argument(
        'input_file', 
        type=str, 
        help="Arquivo PDF de entrada."
    )

    parser.add_argument(
        'output_folder', 
        type=str, 
        help="Pasta de saída para o texto e as imagens extraídas."
    )

    return parser.parse_args()

def main():
    args = parse_arguments()
    extractor = PDFExtractor(args.input_file, args.output_folder)
    extractor.extract_text_and_images()

if __name__ == "__main__":
    main()
