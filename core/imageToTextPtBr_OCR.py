
"""
por padrao pega o ultimo screenshot da pasta capturas de tela no onedrive

É necessário ter a key json de uma conta de serviço no path abaixo

"""

import argparse
import subprocess
import json
import os
from glob import glob

def detect_text(image_path):
    # Importa a biblioteca
    from google.cloud import vision

    # Cria um cliente Vision
    client = vision.ImageAnnotatorClient()

    # Abre a imagem
    with open(image_path, "rb") as image_file:
        content = image_file.read()

    # Cria uma solicitação de detecção de texto
    image = vision.Image(content=content)

    # Realiza a detecção de texto
    response = client.text_detection(image=image)

    # Imprime o texto detectado
    texts = response.text_annotations
    # for text in texts:
        # print(text.description)

    return texts

def translate_text(target: str, text: str) -> dict:
    """Translates text into the target language.

    Target must be an ISO 639-1 language code.
    See https://g.co/cloud/translate/v2/translate-reference#supported_languages
    """
    from google.cloud import translate_v2 as translate

    translate_client = translate.Client()

    if isinstance(text, bytes):
        text = text.decode("utf-8")

    # Text can also be a sequence of strings, in which case this method
    # will return a sequence of results for each text.
    result = translate_client.translate(text, target_language=target)

    print("Text: {}".format(result["input"]))
    print("Translation: {}".format(result["translatedText"]))
    print("Detected source language: {}".format(result["detectedSourceLanguage"]))

    return result


def main():
    # Encontra a imagem mais recente na pasta de screenshots
    screenshot_path = os.path.join('C:\\', 'Users', 'user', 'OneDrive', 'images', 'Screenshots', 'tyrania')
    images = glob(os.path.join(screenshot_path, '*.png'))  # Filtra por arquivos PNG
    latest_image = max(images, key=os.path.getctime) if images else None
    
    if not latest_image:
        print("Nenhuma imagem encontrada na pasta de screenshots.")
        return
    
    # Configura o argparse
    parser = argparse.ArgumentParser(description='Detecta texto em uma imagem usando o Google Cloud Vision API.')
    parser.add_argument('image_path', type=str, nargs='?', help='Caminho para a imagem a ser analisada.', default=latest_image)
    
    # Analisa os argumentos da linha de comando
    args = parser.parse_args()
    
    # Chama a função de detecção de texto
    # try:
    for i in range(1):
        result = detect_text(args.image_path)
        # print(json.dumps(result, indent=2))
        # with open(r"C:\Users\user\OneDrive\swap.json", 'w') as f:
            # f.write(json.dumps(result, indent=2))
        # texts = json.dumps(result, indent=2)
        # print(dir(result))
        # texts = result['responses'][0]['textAnnotations']
        # print(texts)
        # x1 = result[0]['description']
        x1 = result[0].description
        # x1 = result['responses'][0]['textAnnotations'][0]['description']
        # x1 = result['responses'][0]['textAnnotations'][0]['description']
        with open(r"C:\Users\user\OneDrive\swap\legendas tyrania youtube.txt", 'a', encoding='utf8') as f:
            f.write(translate_text('pt-BR', x1)["translatedText"])
            f.write('\n')
        # for text in texts:
            # print(f'\n"{text['description']}"', end=' | ')

            # vertices = [
                # f"({vertex.x},{vertex.y})" for vertex in text.boundingPoly.vertices
            # ]

            # print("bounds: {}".format(",".join(vertices)))
    # except Exception as e:
        # print(f"Erro: {e}")

if __name__ == "__main__":
    main()
