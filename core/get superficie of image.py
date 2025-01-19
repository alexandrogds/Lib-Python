import cv2
import numpy as np
from sklearn.cluster import KMeans

# Carregar a imagem
imagem = cv2.imread(r"C:\Users\user\Downloads\Code_Anime (1).jpg")
imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

# Transformar a imagem em um array bidimensional de pixels
pixels = imagem_hsv.reshape(-1, 3)

# Aplicar K-means para clusterizar as cores
k = 1  # Número de clusters
kmeans = KMeans(n_clusters=k)
kmeans.fit(pixels)
cor_dominante = kmeans.cluster_centers_[0].astype(int)

# Definir intervalo de cores com base na cor dominante
tolerancia = 30  # Ajuste a tolerância conforme necessário
cor_baixa = np.maximum(cor_dominante - tolerancia, 0)
cor_alta = np.minimum(cor_dominante + tolerancia, 255)

print(f'Cor dominante (HSV): {cor_dominante}')
print(f'Intervalo de cores a serem detectadas: {cor_baixa} a {cor_alta}')

# Criar máscara para a cor dominante
mascara = cv2.inRange(imagem_hsv, cor_baixa, cor_alta)

# Encontrar contornos
contornos, _ = cv2.findContours(mascara, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Identificar o contorno com a maior área
maior_contorno = max(contornos, key=cv2.contourArea)

# Desenhar o contorno maior na imagem original
cv2.drawContours(imagem, [maior_contorno], -1, (0, 255, 0), 3)

# Mostrar a imagem com o contorno
cv2.imshow('Maior área da mesma cor', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()
