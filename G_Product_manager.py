from H_Product_Manager_Bot import *
from D_Category import *
from E_Suppliers import *
from F_Product import *
class Product_manager:

    connection_name = 'LojaDoRenan.db'
    table_category = 'Categorias Produtos'
    table_supplier = 'Fornecedor'
    table_products = 'Produtos'
    category_functions = Category()
    supplier_functions = Suppliers()
    sql_bot = SqlBot()
    connection = sql_bot.create_connetion(connection_name)

    def __init__(self):
        self.option = None
        self.sql_bot = SqlBot()
        self.product_bot = Product_Manager_Bot()

    def product_alteration_menu(self):
        while True:
            basic_interface('alteração de produto')
            print('\n1 - Adicionar produto \n2 - Atualizar produto\n3 - Remover produto\n 4 - Voltar')
            print('__' * 30)
            option = numeric_option(1, 4)
            self.option = option
            if self.option == 1:
                self.insert_product()
            elif self.option == 2:
                self.update_product_menu()
            elif self.option == 3:
                self.delete_product_menu()
            elif self.option == 4:
                break

    def insert_product(self):
        while True:
            basic_interface('adicionar produtos')
            basic_interface('1 - Adicionar produto a categoria e fornacedor existentes'
                            '\n2 - Adicionar produto a categoria existente e CRIAR NOVO FORNECEDOR'
                            '\n3 - Adicionar produto a fornecedor existete e CRIAR NOVA CATEGORIA'
                            '\n4 - Criar novva categoria e novo fornecedor para produto'
                            '\n5 - Voltar')
            option = numeric_option(1,5)
            self.option =option
            if self.option == 1:
                product_name = self.insert_new_product_name()
                sale_price = self.insert_new_product_price()
                amount = self.insert_new_product_amount()
                category_product_id = self.search_category_for_product()
                supplier_product_id = self.search_supplier_for_product()
                self.creating_product_dictionary(product_name,sale_price,amount,category_product_id,supplier_product_id)
            elif self.option == 2:
                product_name = self.insert_new_product_name()
                sale_price = self.insert_new_product_price()
                amount = self.insert_new_product_amount()
                category_product_id = self.search_category_for_product()
                supplier = self.supplier_functions.insert_supplier(for_new_product=product_name)
                supplier_product_id = self.product_bot.select_new_supplier_id(supplier)
                self.creating_product_dictionary(product_name,sale_price,amount,
                                                 category_product_id=category_product_id,
                                                 supplier_product_id=supplier_product_id)
            elif self.option == 3:
                product_name = self.insert_new_product_name()
                sale_price = self.insert_new_product_price()
                amount = self.insert_new_product_amount()
                supplier_product_id = self.search_supplier_for_product()
                category = self.category_functions.insert_category(for_new_product=product_name)
                category_product_id = self.product_bot.select_new_category_id(category)
                self.creating_product_dictionary(product_name, sale_price, amount,
                                                 category_product_id=category_product_id,
                                                 supplier_product_id=supplier_product_id)
            elif self.option == 4:
                product_name = self.insert_new_product_name()
                sale_price = self.insert_new_product_price()
                amount = self.insert_new_product_amount()
                category = self.category_functions.insert_category(for_new_product=product_name)
                category_product_id = self.product_bot.select_new_category_id(category)
                supplier = self.supplier_functions.insert_supplier(for_new_product=product_name)
                supplier_product_id = self.product_bot.select_new_supplier_id(supplier)
                self.creating_product_dictionary(product_name,sale_price,amount,
                                                 category_product_id=category_product_id,
                                                 supplier_product_id=supplier_product_id)
            elif self.option == 5:
                break

    def insert_new_product_name(self):
        product_name = input('Nome do novo produto: ')
        return product_name

    def insert_new_product_price(self):
        sale_price = read_price('Preço de venda: ')
        return sale_price

    def insert_new_product_amount(self):
        amount = read_int('Quantidade: ')
        return amount

    def search_category_for_product(self):
        print(' ')
        self.sql_bot.create_connetion(self.connection_name)
        print ('PROCURANDO A CATEGORIA PARA ADICIONAR PRODUTO'.center(60))
        category_filter = Category()
        category_filter.categories_consult_menu()
        category_product_id = read_int('ID da categoria que deseja cadastrar o produto')
        return category_product_id

    def search_supplier_for_product(self):
        print(' ')
        self.sql_bot.create_connetion(self.connection_name)
        print ('PROCURANDO O FORNECEDOR PARA ADICIONAR PRODUTO')
        supplier_filter = Suppliers()
        supplier_filter.supplier_consult_menu()
        supplier_product_id = read_int('ID do fonecedor que deseja cadastrar o produto')
        return supplier_product_id

    def creating_product_dictionary(self, product_name, sale_price, amount, category_product_id, supplier_product_id):
        new_prodcuct = Product(product_name,sale_price,amount,category=category_product_id,supplier=supplier_product_id)
        dic = new_prodcuct.__dict__
        print(dic)
        self.product_bot.insert_product_new_new(dic,category_product_id,supplier_product_id)
        return dic

    def product_filter_menu(self):
        while True:
            basic_interface('estoque - filtros de consulta de produto')
            print('__' * 30)
            print(
                '\n1 - Ver todos os produtos\n2 - Buscar por nome\n3 - Buscar por id\n4 - Buscar por categoria\n5 - Buscar por fornecedores\n6 - Sair')
            option = numeric_option(1, 6)
            self.option = option
            if self.option == 1:
                self.product_bot.product_show_all()
                break
            elif self.option == 2:
                self.product_bot.select_product_by(by_product_name=True)
                break
            elif self.option == 3:
                self.product_bot.select_product_by(by_prodduct_id=True)
                break
            elif self.option == 4:
                self.product_bot.select_product_by(by_category=True)
                break
            elif self.option == 5:
                self.product_bot.select_product_by(by_supplier=True)
                break
            elif self.option == 6:
                break



    def update_product_menu(self):
        while True:
            basic_interface('Busca do produto que deseja alterar')
            self.product_filter_menu()
            product = input('ID do produto que deseja alterar:')
            basic_interface('1 - Alterar nome\n2- Alterar Preço\n3 - Alterar quantidade\n4 - Alterar Categoria\n5 - Alterar Fornecedor\n6 - Voltar')
            option = numeric_option(1,6)
            self.option = option
            if self.option == 1:
                self.product_bot.simple_update_product(product, uptade_name=True)
                break
            elif self.option == 2:
                self.product_bot.simple_update_product(product, update_price=True)
                break
            elif self.option == 3:
                self.product_bot.simple_update_product(product, update_amount=True)
                break
            elif self.option == 4:
                self.product_bot.simple_update_product(product, update_category=True)
                break
            elif self.option == 5:
                self.product_bot.simple_update_product(product, update_supplier=True)
                break
            elif self.option == 6:
                break


    def product_without(self):
        if not self.connection:
            self.connection = self.sql_bot.create_connetion(self.connection_name)
        cur = self.connection.cursor()
        cur.execute(''' select * from Produtos where id_categoria is null''')
        result = cur.fetchall()
        if result == []:
            pass
        else:
            print('Ops, só para avisar, encontrei esses produtos sem categoria :) ')
            for product in result:
                print(f'ID = {product[0]} Nome = {product[3]}')
        cur.execute(''' select * from Produtos where id_fornecedor is null''')
        result = cur.fetchall()
        if result == []:
            pass
        else:
            print('Ops, só para avisar, encontrei esses produtos sem fornecedor :) ')
            for product in result:
                print(f'ID = {product[0]} Nome = {product[3]}')

    def delete_product_menu(self):
        while True:
            empty = self.sql_bot.select_all_table('Produtos')
            if empty:
                break
            initial_interface('menu de deleção de produtos')
            print('1 - Deletar um produto\n2 - Deletar todos os produtos sem categoria\n3 - Deletar todos os produtos sem fornecedor'
                  '\n4 - Deletar todos os produtos\n 5 - Voltar')
            option = numeric_option(1,5)
            self.option = option
            if self.option == 5:
                break
            elif self.option == 1:
                self.product_filter_menu()
                self.sql_bot.delete_one_row('Produtos','ID do produto que deseja deletar')
            elif self.option == 2:
                self.product_bot.product_show_all(without_category=True)
                self.product_bot.delete_all_products_without(without_category=True)
            elif self.option == 3:
                self.product_bot.product_show_all(without_supplier=True)
                self.product_bot.delete_all_products_without(without_supplier=True)
            elif self.option == 4:
                self.sql_bot.delete_all_rows_from_a_table('Produtos')































