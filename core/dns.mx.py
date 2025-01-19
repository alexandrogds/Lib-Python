import dns.resolver

def check_mx_records(domain):
    try:
        # Consulta os registros MX do domínio
        mx_records = dns.resolver.resolve(domain, 'MX')
        
        # Imprime os registros MX encontrados
        print("Registros MX para o domínio", domain)
        for mx_record in mx_records:
            print("Host:", mx_record.exchange, "Prioridade:", mx_record.preference)
    except dns.resolver.NoAnswer:
        print("Nenhum registro MX encontrado para o domínio", domain)
    except dns.resolver.NXDOMAIN:
        print("O domínio", domain, "não existe.")
    except dns.resolver.Timeout:
        print("Tempo limite de consulta excedido para o domínio", domain)
    except Exception as e:
        print("Erro ao consultar registros MX:", e)

# Exemplo de uso
import sys
domain = sys.argv[1]
check_mx_records(domain)
