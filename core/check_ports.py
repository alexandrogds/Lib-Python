import socket

def check_port(domain, port):
    # Cria um objeto socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Tenta conectar ao domínio e porta especificados
        result = s.connect_ex((domain, port))

        # Verifica se a conexão foi bem-sucedida
        if result == 0:
            print(f"The door {port} in {domain} is opened")
        else:
            print(f"The door {port} in {domain} is closed.")
    except socket.error as e:
        print(f"Ocorreu um erro ao tentar conectar: {e}")
    finally:
        # Fecha o socket
        s.close()

# Domínio e porta a serem verificados
import sys
domain = sys.argv[1]
port = int(sys.argv[2])

# Chama a função para verificar a porta
check_port(domain, port)
# is closed.