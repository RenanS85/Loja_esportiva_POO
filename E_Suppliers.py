from J_uteis import *
from I_SqliteBot import *
class Suppliers:
    connection_name = 'LojaDoRenan.db'
    table_supplier = 'Fornecedor'

    def __init__(self):
        self.option = None
        self.sql_bot = SqlBot()
        self.supplier_bot = SupplierBot()

    def suplier_alteration_menu(self):
        while True:
            basic_interface('alteração de fornecedores')
            print('\n1 - Adicionar fornecedor \n2 - Atualizar fornecedor\n3 - Remover fornecedor\n 4 - Voltar')
            print('__' * 30)
            option = numeric_option(1, 4)
            self.option = option
            if self.option == 1:
                self.insert_supplier()
            elif self.option == 2:
                self.update_supplier_menu()
            elif self.option == 3:
                self.delete_supplier_menu()
            elif self.option == 4:
                break




    def supliers_filter_menu(self):
        basic_interface('estoque - filtros de consulta de fornecedores')
        print('__' * 30)
        print('\n1 - Ver todos os fornecedores\n2 - Buscar por categoria\n3 - Buscar por nome\n4 - Buscar por id\n5 - Voltar')
        option = numeric_option(1, 5)
        self.option = option
        return option

    def insert_supplier(self,for_new_product=False,do_again=False):
        while True:
            if not for_new_product:
                print('CRIANDO NOVO FORNECEDOR'.center(60))
            else:
                print(f'CRIANDO NOVO FORNECEDOR PARA {for_new_product}'.center(60))
            self.sql_bot.create_connetion(self.connection_name)
            see_table_suppliers = yes_or_not_option('Ver tabela de fornecedores? :')
            if see_table_suppliers == 'S':
                self.sql_bot.select_all_table(self.table_supplier,show_result=True)
            supplier = self.sql_bot.insert_category_or_supplier_data(self.table_supplier, 'Nome do novo fornecedor: ')
            if do_again:
                do_again = yes_or_not_option('Adicionar outro fornecedor?: ')
                if do_again == 'S':
                    continue
                else:
                    break
            else:
                break
        return supplier

    def filter_suplier_by_category_menu(self):
        basic_interface('estoque - filtros de consulta de fornecedor por categoria')
        print('__' * 30)
        print('\n1 - Ver todos as categorias\n2 - Buscar por nome da categorias')
        option = numeric_option(1, 5)
        self.option = option

    def update_supplier_menu(self):
        while True:
            self.sql_bot.create_connetion(self.connection_name)
            basic_interface('atualização de fornecedores')
            self.supliers_filter_menu()
            if self.option == 5:
                break
            if self.option == 1:
                self.sql_bot.select_all_table(self.table_supplier,show_result=True)
                self.sql_bot.update_stock_data(self.table_supplier, 'ID do fornecedor que deseja alterar: ',
                                           "Nome do novo fornecedor: ")
            elif self.option == 2:
                self.filter_suplier_by_category_menu()
                if self.option == 1:
                    self.supplier_bot.show_all_suppliers_by_categories()
                    self.sql_bot.update_stock_data(self.table_supplier, 'ID do fornecedor que deseja alterar: ',
                                               "Nome do novo fornecedor: ")
                elif self.option == 2:
                    self.supplier_bot.show_suppliers_by_categories_names('Digite o nome da categoria: ')
                    self.sql_bot.update_stock_data(self.table_supplier, 'ID do fornecedor que deseja alterar: ',
                                               "Nome do novo fornecedor: ")
            elif self.option == 3:
                self.sql_bot.select_data_by_name(self.table_supplier, 'nome', 'Digite o nome do fornecedor: ')
                self.sql_bot.update_stock_data(self.table_supplier, 'ID do fornecedor que deseja alterar: ',
                                           "Nome do novo fornecedor: ")
            elif self.option == 4:
                self.sql_bot.select_data_by_id(self.table_supplier, 'ID para busca: ')
                self.sql_bot.update_stock_data(self.table_supplier, 'ID do fornecedor que deseja alterar: ',
                                           "Nome do novo fornecedor: ")
            do_again = yes_or_not_option('Atualizar mais fornecedores?: ')
            if do_again == 'S':
                continue
            else:
                break

    def delete_supplier_menu(self):
        while True:
            self.sql_bot.create_connetion(self.connection_name)
            basic_interface('deletar fornecedor')
            print('1 - Filtrar fornecedor\n 2 - Deletar todos os fornecedores\n3 - Voltar')
            option = numeric_option(1,3)
            if option == 3:
                break
            elif option == 1:
                self.supliers_filter_menu()
                if self.option == 6:
                    break
                if self.option == 1:
                    self.sql_bot.select_all_table(self.table_supplier,show_result=True)
                elif self.option == 2:
                    self.filter_suplier_by_category_menu()
                    if self.option == 1:
                        self.supplier_bot.show_all_suppliers_by_categories()
                    elif self.option == 2:
                        self.supplier_bot.show_suppliers_by_categories_names('Digite o nome da categoria: ')
                elif self.option == 3:
                    self.sql_bot.select_data_by_name(self.table_supplier, 'nome', 'Digite o nome do fornecedor: ')
                elif self.option == 4:
                    self.sql_bot.select_data_by_id(self.table_supplier, 'ID para busca: ')
                self.sql_bot.delete_one_row(self.table_supplier, 'ID do fornecedor que desja apagar: ',
                                            delete_product_supplier=True)
                do_again = yes_or_not_option('Deletar mais fornecedores?: ')
                if do_again == 'S':
                    continue
                else:
                    break
            elif option == 2:
                self.sql_bot.delete_all_rows_from_a_table(self.table_supplier,delete_supplier=True)

    def supplier_consult_menu(self,do_again_question=False):
        while True:
            self.sql_bot.create_connetion(self.connection_name)
            empty = self.sql_bot.select_all_table(self.table_supplier)
            if empty:
                print('Ops, não há fornecedores cadastrados')
                break
            self.supliers_filter_menu()
            if self.option == 4:
                break
            elif self.option == 1:
                self.sql_bot.select_all_table(self.table_supplier,show_result=True)
            elif self.option == 2:
                self.filter_suplier_by_category_menu()
                if self.option == 1:
                    self.supplier_bot.show_all_suppliers_by_categories()
                elif self.option == 2:
                    self.supplier_bot.show_suppliers_by_categories_names('Digite o nome da categoria')
            elif self.option == 3:
                self.sql_bot.select_data_by_name(self.table_supplier, 'nome', 'Digite o nome do fornecedor: ')
            elif self.option == 4:
                self.sql_bot.select_data_by_id(self.table_supplier, "ID do fornecedor: ")
            if do_again_question:
                do_again = yes_or_not_option('Deseja consultar novamente?')
                if do_again == 'S':
                    continue
                else:
                    break
            if not do_again_question:
                break


class SupplierBot:
    connection_name = 'LojaDoRenan.db'
    sql_bot = SqlBot()
    connection = sql_bot.create_connetion(connection_name)

    def show_all_suppliers_by_categories(self):
        id_suppiler = 'p.id_fornecedor'
        fornecedor = 'f.nome as Fornecedor'
        categoria = 'cp.nome as Categoria'
        try:
            cur = self.connection.cursor()
            cur.execute(f'''SELECT p.id_fornecedor, f.nome as Fornecedor, cp.nome as Categoria
from Produtos p , "Categorias Produtos" cp, Fornecedor f 
WHERE p.id_categoria = cp.id and p.id_fornecedor = f.id;''')
        except sqlite3.Error as er:
            print(er)
        else:
            result = cur.fetchall()
            print('id Fornecedor'.center(20), 'Fornecedor'.center(20), 'Categoria'.center(20))
            c = 0
            for c in result:
                id_column = c[0]
                category_column = c[1]
                fornecedor_column = c[2]
                print(f'{id_column:^20}| {category_column:^20}| {fornecedor_column:^20}')

    def show_suppliers_by_categories_names(self, txt_category_name):
        category = input(txt_category_name)
        if self.connection:
            try:
                cur = self.connection.cursor()
                cur.execute(f'''SELECT p.id_fornecedor, f.nome as Fornecedor, cp.nome as Categoria
    from Produtos p , Fornecedor f , "Categorias Produtos" cp
    WHERE p.id_fornecedor = f.id and p.id_categoria = cp.id and cp.nome LIKE "{category}%"''')
            except sqlite3.Error as er:
                print(er)
            else:
                result = cur.fetchall()
                if result == []:
                    print('OPS, ainda não há um produto com esse foencedor vinculado a uma categoria!')
                else:
                    print('id Fornecedor'.center(20), 'Fornecedor'.center(20), 'Categoria'.center(20))
                    c = 0
                    for c in result:
                        id_column = c[0]
                        fornecedor_column = c[1]
                        category_column = c[2]
                        print(f'{id_column:^20}| {fornecedor_column:^20}| {category_column:^20}')
