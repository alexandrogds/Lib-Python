import socket
import sys
import threading
import psutil
import os

def reverse_dns_lookup(ip_address):
    try:
        # Realiza a consulta de DNS reverso
        hostname, aliases, addresses = socket.gethostbyaddr(ip_address)
        o = hostname, aliases, addresses
        print(ip_address, ':', o)
        project_id = 'big-table-encoding'
        instance_id = 'big-table-encoding'
        table_id = ''
        #bt_manager = BigtableManager(project_id, instance_id, table_id)
        #bt_manager.insert_data(args.row_key, args.data)
        #with open("C:\\Users\\user\\OneDrive\\sources\\datas\\all_ips_and_domains.txt", 'a') as f:
        #    f.write(ip + ',' + str(o) + '\n')
    except socket.herror:
        return "Não foi possível encontrar o DNS reverso para o endereço IP {}".format(ip_address)

def main():
    threads = []
    for _1 in range(14, 39):
        for _2 in range(0,256):
            for _3 in range(0,256):
                for _4 in range(0,256):
                    memoria = psutil.virtual_memory()
                    memoria_disponivel = memoria.available
                    memoria_disponivel_gb = memoria_disponivel / (1024 ** 3)
                    if memoria_disponivel_gb < 1:
                        input('espere a memória ser liberada e tecle enter para continuar')
                    ip = '.'.join([str(_1),str(_2),str(_3),str(_4)])
                    t = threading.Thread(target=reverse_dns_lookup, args=(ip,))
                    threads.append(t)
                    t.start()

    for t in threads:
        t.join()

    print("Todas as threads foram finalizadas.")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        file = os.path.basename(sys.argv[0])
        print(f'use: {file} [ip])|all')
    elif sys.argv[1] == 'all':
        main()
    else:
        ip = sys.argv[1]
        reverse_dns_lookup(ip)