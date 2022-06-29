from J_uteis import *
from I_SqliteBot import *


class Category:
    connection_name = 'LojaDoRenan.db'
    table_category = 'Categorias Produtos'

    def __init__(self):
        self.option = None
        self.sql_bot = SqlBot()
        self.category_bot = CategoryBot()

    def categories_alteration_menu(self):
        while True:
            basic_interface('alteração de categorias')
            print('\n1 - Adicionar categoria \n2 - Atualizar categoria\n3 - Remover categoria\n 4 - Voltar')
            print('__' * 30)
            option = numeric_option(1, 4)
            self.option = option
            if self.option == 1:
                self.insert_category()
            elif self.option == 2:
                self.update_category_menu()
            elif self.option == 3:
                self.delete_category_menu()
            elif self.option == 4:
                break

    def categories_filter_menu(self):
        basic_interface('estoque - filtros de consulta de categoria')
        print('__' * 30)
        print(
            '\n1 - Ver todas categorias\n2 - Buscar por nome\n3 - Buscar por id\n4 - Buscar por fornecedores\n5 - Sair')
        option = numeric_option(1, 5)
        self.option = option
        return option


    def insert_category(self,for_new_product=False, do_again = False):
        while True:
            if not for_new_product:
                print('CRIANDO NOVO FORNECEDOR'.center(60))
            else:
                print(f'CRIANDO NOVO FORNECEDOR PARA {for_new_product}'.center(60))
            self.sql_bot.create_connetion(self.connection_name)
            see_table_categories = yes_or_not_option('Ver tabela de categprias? :')
            if see_table_categories == 'S':
                self.sql_bot.select_all_table(self.table_category,show_result=True)
            category = self.sql_bot.insert_category_or_supplier_data(self.table_category, 'Nome da nova categoria: ')
            if do_again:
                do_again = yes_or_not_option('Adicionar outro fornecedor?: ')
                if do_again == 'S':
                    continue
                else:
                    break
            else:
                break
        return category

    def filter_category_by_suplier_menu(self):
        basic_interface('estoque - filtros de consulta de categoria por fornecedor')
        print('__' * 30)
        print('\n1 - Ver todos os fonecedores\n2 - Buscar por nome de fornecedor')
        option = numeric_option(1, 5)
        self.option = option

    def update_category_menu(self):
        while True:
            self.sql_bot.create_connetion(self.connection_name)
            basic_interface('atualização de categoria')
            self.categories_filter_menu()
            if self.option == 5:
                break
            elif self.option == 1:
                self.sql_bot.select_all_table(self.table_category,show_result=True)
                self.sql_bot.update_stock_data(self.table_category, 'ID da categoria que deseja alterar: ',
                                           "Nome da nova categoria: ")
            elif self.option == 2:
                self.sql_bot.select_data_by_name(self.table_category, 'nome', 'Digite o nome da categoria: ')
                self.sql_bot.update_stock_data(self.table_category, 'ID da categoria que deseja alterar: ',
                                           "Nome da nova categoria: ")
            elif self.option == 3:
                self.sql_bot.select_data_by_id(self.table_category, 'ID para busca: ')
                self.sql_bot.update_stock_data(self.table_category, 'ID da categoria que deseja alterar: ',
                                           "Nome da nova categoria: ")
            elif self.option == 4:
                self.filter_category_by_suplier_menu()
                if self.option == 1:
                    self.category_bot.show_all_categories_by_supplier()
                    self.sql_bot.update_stock_data(self.table_category, 'ID da categoria que deseja alterar: ',
                                               "Nome da nova categoria: ")
                elif self.option == 2:
                    self.category_bot.show_categories_by_SupplierName('Digite o nome do fornecedor')
                    self.sql_bot.update_stock_data(self.table_category, 'ID da categoria que deseja alterar: ',
                                               "Nome da nova categoria: ")
            do_again = yes_or_not_option('Atualizar mais categorias?: ')
            if do_again == 'S':
                continue
            else:
                break

    def delete_category_menu(self):
        while True:
            self.sql_bot.create_connetion(self.connection_name)
            basic_interface('deletar categoria')
            print('1 - Filtrar categoria\n 2 - Deletar todas as categorias\n3 - Voltar')
            option = numeric_option(1, 3)
            if option == 3:
                break
            elif option == 1:
                self.categories_filter_menu()
                if self.option == 4:
                    break
                elif self.option == 1:
                    self.sql_bot.select_all_table(self.table_category,show_result=True)
                elif self.option == 2:
                    self.sql_bot.select_data_by_name(self.table_category, 'nome', 'Digite o nome da categoria: ')
                elif self.option == 3:
                    self.sql_bot.select_data_by_id(self.table_category, 'ID para busca: ')
                elif self.option == 4:
                    self.filter_category_by_suplier_menu()
                    if self.option == 1:
                        self.category_bot.show_all_categories_by_supplier()
                    elif self.option == 2:
                        self.category_bot.show_categories_by_SupplierName('Digite o nome do fornecedor: ')
                self.sql_bot.delete_one_row(self.table_category, 'ID da categegoria a deletar: ', delete_product_category=True)
                do_again = yes_or_not_option('Deletar mais categorias?: ')
                if do_again == 'S':
                    continue
                else:
                    break
            elif option == 2:
                self.sql_bot.delete_all_rows_from_a_table(self.table_category,delete_category=True)

    def categories_consult_menu(self,do_again_question=False):
        while True:
            self.sql_bot.create_connetion(self.connection_name)
            empty = self.sql_bot.select_all_table(self.table_category)
            if empty == True:
                print ('Ops, não há categorias cadastradas')
                break
            else:
                self.categories_filter_menu()
                if self.option == 4:
                    break
                elif self.option == 1:
                    self.sql_bot.select_all_table(self.table_category,show_result=True)
                elif self.option == 2:
                    self.sql_bot.select_data_by_name(self.table_category, 'nome', 'Digite o nome da categoria: ')
                elif self.option == 3:
                    self.sql_bot.select_data_by_id(self.table_category, 'ID para busca: ')
                elif self.option == 4:
                    self.filter_category_by_suplier_menu()
                    if self.option == 1:
                        self.category_bot.show_all_categories_by_supplier()
                    elif self.option == 2:
                        self.category_bot.show_categories_by_SupplierName('Digite o nome do fornecedor')
                if do_again_question:
                    do_again = yes_or_not_option('Deseja consultar novamente?')
                    if do_again == 'S':
                        continue
                    else:
                        break
                if not do_again_question:
                    break

class CategoryBot:
    connection_name = 'LojaDoRenan.db'
    sql_bot = SqlBot()
    connection = sql_bot.create_connetion(connection_name)


    def show_all_categories_by_supplier(self):
        id_categoria = 'p.id_categoria'
        categoria = 'cp.nome as Categoria'
        fornecedor = 'f.nome as fornecedor'
        try:
            cur = self.connection.cursor()
            cur.execute(f'''SELECT {id_categoria}, {categoria}, {fornecedor}
from Produtos p , "Categorias Produtos" cp, Fornecedor f 
WHERE p.id_categoria = cp.id and p.id_fornecedor = f.id ;''')
        except sqlite3.Error as er:
            print(er)
        else:
            result = cur.fetchall()
            print('id Categoria'.center(20), 'Categoria'.center(20), 'Fornecedor'.center(20))
            if result == []:
                print('OPS, ainda não há um produto com essa cataegoria vinculada a um fornecedor!')
            else:
                c = 0
                for c in result:
                    id_column = c[0]
                    category_column = c[1]
                    fornecedor_column = c[2]
                    print(f'{id_column:^20}| {category_column:^20}| {fornecedor_column:^20}')

    def show_categories_by_SupplierName(self, txt_supplier_name):
        suplier_name = input(txt_supplier_name)
        id_categoria = 'p.id_categoria'
        categoria = 'p.id_categoria'
        fornecedor = 'p.id_categoria'
        try:
            cur = self.connection.cursor()
            cur.execute(f'''SELECT p.id_categoria, p.id_categoria, p.id_categoria
from Produtos p , "Categorias Produtos" cp, Fornecedor f 
WHERE p.id_categoria = cp.id and p.id_fornecedor = f.id and f.nome like "{suplier_name}%" ;''')
        except sqlite3.Error as er:
            print(er)
        else:
            result = cur.fetchall()
            print('id Categoria'.center(20), 'Categoria'.center(20), 'Fornecedor'.center(20))
            c = 0
            for c in result:
                id_column = c[0]
                category_column = c[1]
                fornecedor_column = c[2]
                print(f'{id_column:^20}| {category_column:^20}| {fornecedor_column:^20}')
