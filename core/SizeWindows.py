import tkinter as tk
import time

def get_window_size():
    root = tk.Tk()
    # Obtém a largura e altura da janela principal
    width = root.winfo_width()
    height = root.winfo_height()
    root.destroy()  # Fecha a janela depois de obter as informações
    return width, height

def get_screen_resolution():
    root = tk.Tk()
    # Obtém a largura e altura total da tela
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.destroy()  # Fecha a janela temporária depois de obter as informações
    return screen_width, screen_height

width, height = get_window_size()
print(f"Largura da janela: {width}px")
print(f"Altura da janela: {height}px")
time.sleep(1)
screen_width, screen_height = get_screen_resolution()
print(f"Largura da tela: {screen_width}px")
print(f"Altura da tela: {screen_height}px")
time.sleep(1)