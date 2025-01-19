import psutil

memoria = psutil.virtual_memory()
memoria_disponivel = memoria.available
memoria_disponivel_gb = memoria_disponivel / (1024 ** 3)
print("Memória disponível:", memoria_disponivel_gb, "GB")
