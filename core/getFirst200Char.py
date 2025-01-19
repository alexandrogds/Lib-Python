import argparse

def read_first_200_chars(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read(200)
            return content
    except FileNotFoundError:
        return f"Erro: O arquivo '{file_path}' não foi encontrado."
    except Exception as e:
        return f"Erro ao ler o arquivo: {e}"

def main():
    parser = argparse.ArgumentParser(description="Lê os primeiros 200 caracteres de um arquivo.")
    parser.add_argument('file_path', type=str, help="Caminho para o arquivo a ser lido.")
    
    args = parser.parse_args()
    
    result = read_first_200_chars(args.file_path)
    print(result)

if __name__ == "__main__":
    main()
