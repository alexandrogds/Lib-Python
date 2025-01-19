import argparse
from PyPDF2 import PdfReader, PdfWriter
import os
import shutil

class PDFManager:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def delete_pages(self, pages_to_delete):
        try:
            # Verifica se o arquivo de entrada existe
            if not os.path.exists(self.input_file):
                raise FileNotFoundError(f"Arquivo não encontrado: {self.input_file}")

            # Caso nenhuma página seja fornecida para exclusão, copie o arquivo
            if not pages_to_delete:
                shutil.copy(self.input_file, self.output_file)
                print(f"Nenhuma página para excluir. O arquivo foi copiado para {self.output_file}")
                return

            # Lê o arquivo PDF
            reader = PdfReader(self.input_file)

            # Verifica se as páginas a serem deletadas são válidas
            num_pages = len(reader.pages)
            for page in pages_to_delete:
                if page < 1 or page > num_pages:
                    raise ValueError(f"Índice de página inválido: {page}. O PDF possui {num_pages} páginas.")

            # Converte os índices para começar em 0
            pages_to_delete = [page - 1 for page in pages_to_delete]

            # Cria um escritor de PDF
            writer = PdfWriter()

            # Adiciona todas as páginas, exceto as que devem ser deletadas
            for i in range(num_pages):
                if i not in pages_to_delete:
                    writer.add_page(reader.pages[i])

            # Escreve o novo arquivo PDF
            with open(self.output_file, 'wb') as output_file:
                writer.write(output_file)

            print(f"Páginas {pages_to_delete} deletadas com sucesso. Novo arquivo salvo como {self.output_file}.")

        except Exception as e:
            print(f"Ocorreu um erro: {e}")

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Script para gerenciar PDFs, permitindo a remoção de páginas específicas."
    )

    parser.add_argument(
        'input_file', 
        type=str, 
        help="Arquivo PDF de entrada."
    )

    parser.add_argument(
        'output_file', 
        type=str, 
        help="Arquivo PDF de saída com as páginas deletadas ou copiado se nenhuma página for fornecida."
    )

    parser.add_argument(
        'pages', 
        type=int, 
        nargs='*', 
        help="Lista de índices de páginas a serem deletadas (começando em 1)."
    )

    return parser.parse_args()

def main():
    args = parse_arguments()
    manager = PDFManager(args.input_file, args.output_file)
    manager.delete_pages(args.pages)

if __name__ == "__main__":
    main()
