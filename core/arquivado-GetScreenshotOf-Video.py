import tkinter as tk
import argparse
import os
from datetime import datetime
from PIL import Image, ImageTk
import cv2

class VideoPlayer:
    def __init__(self, janela, caminho_video, pasta_screenshots):
        self.janela = janela
        self.caminho_video = caminho_video
        self.pasta_screenshots = pasta_screenshots
        self.frame_atual = None
        self.playing = True

        self.canvas = tk.Canvas(janela)
        self.canvas.pack()

        self.botao_play = tk.Button(janela, text="Play", command=self.toggle_play_pause)
        self.botao_play.pack(side=tk.LEFT)

        self.botao_screenshot = tk.Button(janela, text="Screenshot", command=self.capturar_screenshot)
        self.botao_screenshot.pack(side=tk.LEFT)

        self.atualizar_frame()

    def atualizar_frame(self):
        frame = self.carregar_proximo_frame()
        if frame is not None:
            self.imagem_tk = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
            self.canvas.config(width=self.imagem_tk.width(), height=self.imagem_tk.height())
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.imagem_tk)
        if self.playing:
            self.janela.after(10, self.atualizar_frame)

    def carregar_proximo_frame(self):
        if self.frame_atual is not None and self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                return frame
        return None

    def toggle_play_pause(self):
        if self.playing:
            self.playing = False
            self.botao_play.config(text="Play")
        else:
            self.playing = True
            self.botao_play.config(text="Pause")
            if self.frame_atual is None:
                self.cap = cv2.VideoCapture(self.caminho_video)
        self.atualizar_frame()

    def capturar_screenshot(self):
        if self.frame_atual is not None:
            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            nome_arquivo = f"{timestamp}.png"
            caminho_salvar = os.path.join(self.pasta_screenshots, nome_arquivo)
            cv2.imwrite(caminho_salvar, self.frame_atual)
            print(f"Screenshot salvo como '{caminho_salvar}'")

def obter_video_mais_recente(pasta_videos):
    videos = [os.path.join(pasta_videos, nome) for nome in os.listdir(pasta_videos) if nome.endswith('.mp4')]
    if not videos:
        return None
    return max(videos, key=os.path.getctime)

def main():
    parser = argparse.ArgumentParser(description='Exibe um vídeo e captura um screenshot do frame ao clicar no vídeo.')
    parser.add_argument('--pasta_videos', type=str, default=r'C:\Users\user\Videos', help='Caminho para a pasta onde os vídeos estão localizados')
    parser.add_argument('--pasta_screenshots', type=str, default=r'C:\Users\user\OneDrive\images\Screenshots', help='Caminho para a pasta onde os screenshots serão salvos')
    parser.add_argument('--caminho_video', type=str, help='Caminho para o vídeo a ser exibido')
    args = parser.parse_args()

    if args.caminho_video is None:
        caminho_video = obter_video_mais_recente(args.pasta_videos)
        if caminho_video is None:
            print("Nenhum vídeo encontrado na pasta especificada.")
            return
    else:
        caminho_video = args.caminho_video

    janela = tk.Tk()
    janela.title("Player de Vídeo")

    player = VideoPlayer(janela, caminho_video, args.pasta_screenshots)

    janela.mainloop()

if __name__ == "__main__":
    main()
