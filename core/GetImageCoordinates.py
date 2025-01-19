import tkinter as tk
import argparse

class Aplicacao:
    def __init__(self, janela, imagem):
        self.janela = janela
        self.imagem = imagem
        self.canvas = tk.Canvas(janela, width=imagem.width(), height=imagem.height())
        self.canvas.pack()
        self.canvas.create_image(0, 0, anchor=tk.NW, image=imagem)
        self.canvas.bind("<Button-1>", self.clique_do_mouse)

    def clique_do_mouse(self, evento):
        x = self.canvas.canvasx(evento.x)
        y = self.canvas.canvasy(evento.y)
        print(f"Coordenadas do clique: ({x}, {y})")

def main():
    parser = argparse.ArgumentParser(description='Exibe uma imagem e retorna as coordenadas dos cliques do mouse.')
    parser.add_argument('caminho_imagem', type=str, help='Caminho para a imagem a ser exibida')
    args = parser.parse_args()

    janela = tk.Tk()
    janela.title("Exibição de Imagem")
    
    # Carregando a imagem
    imagem = tk.PhotoImage(file=args.caminho_imagem)

    app = Aplicacao(janela, imagem)

    janela.mainloop()

if __name__ == "__main__":
    main()
