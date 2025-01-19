import argparse
import os
import subprocess

def extrair_frame(video_path, tempo, pasta_saida):
    # Converter o tempo para segundos
    horas, minutos, segundos = map(int, tempo.split(':'))
    tempo_segundos = horas * 3600 + minutos * 60 + segundos# + 0.5
    
    # Criar a pasta de saída se não existir
    os.makedirs(pasta_saida, exist_ok=True)
    
    # Nome do arquivo de saída
    nome_arquivo = f'frame_{tempo.replace(":", "_")}.jpg'
    caminho_saida = os.path.join(pasta_saida, nome_arquivo)
    
    # Comando ffmpeg para extrair o frame
    comando = [
        'ffmpeg',
        '-i', video_path,
        '-ss', str(tempo_segundos),
        '-vframes', '1',
        caminho_saida
    ]
    
    # Executar o comando
    subprocess.run(comando, check=True)

def main():
    # Configurar o parser de argumentos
    parser = argparse.ArgumentParser(description='Extrai um frame de um vídeo dado o tempo e salva em uma pasta especificada.')
    parser.add_argument('video', type=str, help='Caminho para o vídeo.')
    parser.add_argument('tempo', type=str, help='Tempo no formato hh:mm:ss.')
    parser.add_argument('pasta_saida', type=str, help='Pasta de saída para o frame.')
    
    # Parse dos argumentos da linha de comando
    args = parser.parse_args()
    
    # Extrair o frame
    extrair_frame(args.video, args.tempo, args.pasta_saida)

if __name__ == "__main__":
    main()
