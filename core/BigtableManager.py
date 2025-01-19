import argparse
import sys
from google.cloud import bigtable
from UUID2 import UUID2

class BigtableManager:
    def __init__(self, project_id, instance_id):
        self.project_id = project_id
        self.instance_id = instance_id
        self.client = bigtable.Client(project=self.project_id, admin=True)
        self.instance = self.client.instance(self.instance_id)
        self.uuid2_generator = UUID2()

    def list_tables(self):
        try:
            tables = self.instance.list_tables()
            if tables:
                print("IDs das tabelas:")
                for table in tables:
                    print(table.table_id)
            else:
                print("Nenhuma tabela encontrada.")
        except Exception as e:
            print(f"Erro ao listar tabelas: {e}")

    def create_table(self, table_id, column_family_id):
        try:
            table = self.instance.table(table_id)
            if not table.exists():
                column_families = {
                    column_family_id: bigtable.column_family.MaxVersionsGCRule(2)
                }
                table.create(column_families=column_families)
                print("Tabela criada com sucesso.")
            else:
                print("Tabela já existe.")
        except Exception as e:
            print(f"Erro ao criar tabela: {e}")
            sys.exit(1)

    def insert_data(self, table_id, data, column_family_id, column_id, row_key=None):
        try:
            table = self.instance.table(table_id)
            if row_key is None:
                row_key = self.uuid2_generator.generate_uuid_v2()
            row = table.direct_row(row_key)
            row.set_cell(column_family_id, column_id.encode('utf-8'), data)
            row.commit()
            print(f"Dados inseridos com sucesso. Chave da linha: {row_key}")
        except Exception as e:
            print(f"Erro ao inserir dados: {e}")

    def fetch_all(self, table_id, column_family_id, column_id):
        try:
            table = self.instance.table(table_id)
            partial_rows = table.read_rows()
            partial_rows.consume_all()
            for row_key, row in partial_rows.rows.items():
                if column_family_id in row.cells and column_id.encode('utf-8') in row.cells[column_family_id]:
                    data = row.cells[column_family_id][column_id.encode('utf-8')][0].value.decode('utf-8')
                    print(f"Row key: {row_key.decode('utf-8')}, Data: {data}")
        except Exception as e:
            print(f"Erro ao buscar dados: {e}")

    def fetch_row(self, table_id, row_key, column_family_id, column_id):
        try:
            table = self.instance.table(table_id)
            row = table.read_row(row_key)
            if row and column_family_id in row.cells and column_id.encode('utf-8') in row.cells[column_family_id]:
                data = row.cells[column_family_id][column_id.encode('utf-8')][0].value.decode('utf-8')
                print(f"Row key: {row_key}, Data: {data}")
            else:
                print(f"Linha com a chave {row_key} não encontrada ou coluna inexistente.")
        except Exception as e:
            print(f"Erro ao buscar a linha: {e}")

    def list_columns(self, table_id):
        try:
            table = self.instance.table(table_id)
            column_families = table.list_column_families()
            if column_families:
                print(f"Colunas na tabela {table_id}:")
                for family_id, family in column_families.items():
                    print(f"Família de colunas: {family_id}")
                    partial_rows = table.read_rows()
                    partial_rows.consume_all()
                    for row_key, row in partial_rows.rows.items():
                        for column_id in row.cells[family_id]:
                            print(f"  Coluna: {column_id.decode('utf-8')}")
            else:
                print(f"Nenhuma família de colunas encontrada na tabela {table_id}.")
        except Exception as e:
            print(f"Erro ao listar colunas: {e}")

    def list_rows(self, table_id):
        try:
            table = self.instance.table(table_id)
            partial_rows = table.read_rows()
            partial_rows.consume_all()
            print(f"Linhas na tabela {table_id}:")
            for row_key in partial_rows.rows.keys():
                print(row_key.decode('utf-8'))
        except Exception as e:
            print(f"Erro ao listar linhas: {e}")

def main():
    parser = argparse.ArgumentParser(description="Gerenciador de Banco de Dados Bigtable")
    parser.add_argument('action', choices=['list_tables', 'create', 'insert', 'fetch_all', 'fetch_row', 'list_columns', 'list_rows'], help="Ação a ser realizada: 'list_tables' para listar tabelas, 'create' para criar tabela, 'insert' para inserir dados, 'fetch_all' para buscar todos os dados, 'fetch_row' para buscar uma linha específica, 'list_columns' para listar colunas de uma tabela, 'list_rows' para listar todas as linhas de uma tabela.")
    parser.add_argument('--row_key', type=str, help="Chave da linha para as ações de inserção e busca de linha específica.")
    parser.add_argument('--data', type=str, help="Os dados a serem inseridos. Necessário se a ação for 'insert'.")
    parser.add_argument('--project_id', type=str, required=True, help="ID do projeto do Google Cloud.")
    parser.add_argument('--instance_id', type=str, required=True, help="ID da instância do Bigtable.")
    parser.add_argument('--table_id', type=str, help="ID da tabela do Bigtable.")
    parser.add_argument('--column_family_id', type=str, required=False, default='cf', help="ID da família de colunas. Padrão é 'cf'.")
    parser.add_argument('--column_id', type=str, required=False, default='data', help="ID da coluna. Padrão é 'data'.")

    args = parser.parse_args()

    bt_manager = BigtableManager(args.project_id, args.instance_id)

    if args.action == 'list_tables':
        bt_manager.list_tables()
    elif args.action == 'create':
        if not args.table_id:
            print("Erro: Para criar uma tabela, o argumento --table_id é necessário.")
            sys.exit(1)
        bt_manager.create_table(args.table_id, args.column_family_id)
    elif args.action == 'insert':
        if not args.table_id or not args.row_key or not args.data:
            print("Erro: Para inserir dados, os argumentos --table_id, --row_key e --data são necessários.")
            sys.exit(1)
        bt_manager.insert_data(args.table_id, args.row_key, args.data, args.column_family_id, args.column_id)
    elif args.action == 'fetch_all':
        if not args.table_id:
            print("Erro: Para buscar todos os dados, o argumento --table_id é necessário.")
            sys.exit(1)
        bt_manager.fetch_all(args.table_id, args.column_family_id, args.column_id)
    elif args.action == 'fetch_row':
        if not args.table_id or not args.row_key:
            print("Erro: Para buscar uma linha específica, os argumentos --table_id e --row_key são necessários.")
            sys.exit(1)
        bt_manager.fetch_row(args.table_id, args.row_key, args.column_family_id, args.column_id)
    elif args.action == 'list_columns':
        if not args.table_id:
            print("Erro: Para listar colunas, o argumento --table_id é necessário.")
            sys.exit(1)
        bt_manager.list_columns(args.table_id)
    elif args.action == 'list_rows':
        if not args.table_id:
            print("Erro: Para listar linhas, o argumento --table_id é necessário.")
            sys.exit(1)
        bt_manager.list_rows(args.table_id)

if __name__ == "__main__":
    main()
