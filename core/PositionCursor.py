import pyautogui

def get_cursor_position():
    # Obtém a posição atual do cursor
    x, y = pyautogui.position()
    return x, y

# Exemplo de uso
x, y = get_cursor_position()
print(f"Posição atual do cursor: x={x}, y={y}")
