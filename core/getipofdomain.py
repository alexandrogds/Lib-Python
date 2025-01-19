import socket

def get_ip_address(domain):
    try:
        # Usa a função gethostbyname para resolver o nome de domínio em um endereço IP
        ip_address = socket.gethostbyname(domain)
        print(f'O IP do domínio {domain} é: {ip_address}')
    except socket.gaierror as e:
        print(f"Ocorreu um erro ao tentar resolver o domínio: {e}")

# Chama a função para obter o endereço IP de um domínio
import sys
get_ip_address(sys.argv[1])
