from G_Product_manager import *
from D_Category import *
from E_Suppliers import *



class Stock:


    def __init__(self):
        self.option = None
        self.bot = SqlBot()
        self.category = Category()
        self.supplier = Suppliers()
        self.product_manager = Product_manager()


    def principal_stock_menu(self):
        while True:
            basic_interface('estoque')
            print('\n1 - Alterar estoque\n2 - Consultar estoque\n3 - Voltar')
            print('__' * 30)
            option = numeric_option(1, 3)
            self.option = option
            if option == 3:
                break
            if self.option == 1:
                self.alteration_stock_menu()
            elif self.option == 2:
                self.stock_consult_menu()

    def alteration_stock_menu(self):
        while True:
            basic_interface('alteração de estoque')
            print('\n1 - Alteração de categorias \n2 - Alteração de fornecedores\n3 - alteração de produtos\n4 - Voltar')
            print('__' * 30)
            option = numeric_option(1, 4)
            self.option = option
            if self.option == 4:
                break
            elif self.option == 1:
                self.category.categories_alteration_menu()
            elif self.option == 2:
                self.supplier.suplier_alteration_menu()
            elif self.option == 3:
                self.product_manager.product_alteration_menu()


    def stock_consult_menu(self):
        while True:
            basic_interface('estoque')
            print('\n1 - Consulta de categorias\n3 - Consulta de fornecedores\n3 - Consulta de produtos\n4 - Voltar')
            print('__' * 30)
            option = numeric_option(1, 4)
            self.option = option
            if self.option == 1:
                self.category.categories_consult_menu(do_again_question=True)
            elif self.option == 2:
                self.supplier.supplier_consult_menu(do_again_question=True)
            elif self.option == 3:
                self.product_manager.product_without()
                self.product_manager.product_filter_menu()
            elif self.option == 4:
                break











