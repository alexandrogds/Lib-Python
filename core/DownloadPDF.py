import argparse
import requests

def download_pdf(url, output_path):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na requisição
        with open(output_path, 'wb') as file:
            file.write(response.content)
        print(f"PDF baixado com sucesso: {output_path}")
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar o PDF: {e}")

def main():
    parser = argparse.ArgumentParser(description="Baixar um PDF dado uma URL.")
    parser.add_argument('url', type=str, help='A URL do PDF que você deseja baixar')
    parser.add_argument('output', type=str, help='O caminho onde o PDF será salvo')
    args = parser.parse_args()
    
    download_pdf(args.url, args.output)

if __name__ == '__main__':
    main()
