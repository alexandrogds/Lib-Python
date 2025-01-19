import uuid
import time
import psutil
import os

class UUID2:
    def __init__(self):
        pass

    @staticmethod
    def _get_all_mac_addresses():
        mac_addresses = []
        # Obtém todos os endereços MAC das interfaces de rede disponíveis
        interfaces = psutil.net_if_addrs()
        for interface in interfaces.values():
            for addr in interface:
                if addr.family == psutil.AF_LINK:
                    mac_addresses.append(addr.address)
        return mac_addresses

    @staticmethod
    def _get_username_and_groups():
        # Obtém o nome de usuário e todos os grupos do usuário
        username = os.getlogin()
        groups = [g.gr_name for g in os.getgrouplist(username)]
        return username, groups

    def generate_uuid_v2(self):
        # Obter o tempo atual em UTC+0
        timestamp = int(time.time())

        # Obter o nome de usuário e todos os grupos do usuário
        username, groups = self._get_username_and_groups()

        # Obter todos os endereços MAC
        mac_addresses = self._get_all_mac_addresses()

        # Gerar um UUID v4
        uuid4 = str(uuid.uuid4()).replace("-", "")  # Remove os hífens

        # Concatenar todos os grupos do usuário com o caractere "|"
        all_groups = '|'.join(groups)

        # Concatenar todos os endereços MAC com o caractere "|"
        all_macs = '|'.join(mac_addresses)

        # Formatar o UUID v2
        uuid2 = f"{timestamp}-{username}-{all_groups}-{all_macs}-{uuid4}"

        return uuid2

# Exemplo de uso
if __name__ == "__main__":
    uuid2 = UUID2().generate_uuid_v2()
    print("UUID v2:", uuid2)
