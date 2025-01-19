
"""Compilador de JavaScript

Melhora a performance do código
"""
import argparse
import os
import shutil
import datetime
import re
def transformar_var_em_let(conteudo):
    # Expressão regular para encontrar declarações de variáveis usando 'var'
    padrao_var = re.compile(r'\bvar\b\s+([a-zA-Z_$][0-9a-zA-Z_$]*)', re.MULTILINE)
    # Substituir 'var' por 'let'
    conteudo_transformado = padrao_var.sub(r'let \1', conteudo)
    # Encontrar todas as variáveis definidas
    padrao_var = re.compile(r'\blet\b\s+([a-zA-Z_$][0-9a-zA-Z_$]*)', re.MULTILINE)
    variaveis = padrao_var.findall(conteudo_transformado)
    # Inserir 'variable = null;' após o último uso de cada variável
    for var in variaveis:
        padrao_uso_var = re.compile(r'\b' + re.escape(var) + r'\b')
        posicoes = [(m.start(), m.end()) for m in padrao_uso_var.finditer(conteudo_transformado)]
        if posicoes:
            # Posição do último uso
            ultimo_uso_pos = posicoes[-1][1]
            # Inserir 'variable = null;' após o último uso
            conteudo_transformado = conteudo_transformado[:ultimo_uso_pos] + f'\n{var} = null;' + conteudo_transformado[ultimo_uso_pos:]
    return conteudo_transformado
def processar_arquivo(arquivo):
    try:
        with open(arquivo, 'r', encoding='utf-8') as file:
            conteudo = file.read()
        conteudo_transformado = transformar_var_em_let(conteudo)
        with open(arquivo, 'w', encoding='utf-8') as file:
            file.write(conteudo_transformado)
        print(f"As declarações 'var' foram transformadas em 'let' no arquivo: {arquivo}")
    except FileNotFoundError:
        print(f"Erro: O arquivo {arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")
def fazer_backup(caminho_arquivo):
    # Cria um timestamp
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    # Define o caminho do backup
    pasta_pai = os.path.dirname(caminho_arquivo)
    pasta_backup = os.path.join(pasta_pai, '.backup')
    os.makedirs(pasta_backup, exist_ok=True)
    nome_arquivo = os.path.basename(caminho_arquivo)
    nome_backup = f"{nome_arquivo}_{timestamp}.bak"
    caminho_backup = os.path.join(pasta_backup, nome_backup)
    shutil.copy2(caminho_arquivo, caminho_backup)
    return caminho_backup
def main():
    parser = argparse.ArgumentParser(description='Transformar todas as declarações de variáveis "var" em "let" em um arquivo JavaScript.')
    parser.add_argument('arquivo', help='O caminho para o arquivo JavaScript a ser transformado.')
    args = parser.parse_args()
    caminho_backup = fazer_backup(args.arquivo)
    print(f"Backup do arquivo criado em: {caminho_backup}")
    processar_arquivo(args.arquivo)
if __name__ == '__main__':
    main()