
"""
clicar no terminal, posicionar o mouse no local das coordenadas desajadas e inserir algo para o input diferente de vazio
"""
import pyautogui
from datetime import datetime

# Função para capturar coordenadas e adicionar timestamps
def capturar_coordenadas_com_timestamp():
    while input():
        # Captura as coordenadas do clique
        x, y = pyautogui.position()
        # Obtém o timestamp atual
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        # Formata a linha com as coordenadas e o timestamp
        linha = f'{timestamp}: X={x}, Y={y}'
        # Imprime a linha
        print(linha)
        # Espera por outro clique
        # pyautogui.click()

# Chama a função para iniciar a captura
capturar_coordenadas_com_timestamp()
