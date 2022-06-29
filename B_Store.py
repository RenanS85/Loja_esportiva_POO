
from C_Stock_methods import *
from Clients import *
from J_uteis import *
from I_SqliteBot import *
class Store:

    bot = SqlBot()
    connection_name = 'LojaDoRenan.db'

    def __init__(self):
        self.option = None
        self.stock = Stock()
        self.cliente_manager = ClientManager()

    def principal_menu(self):
            initial_interface('loja do renan')
            print ('1 - Estoque\n2 - Cadastro de cliente\n3 - Vender Produto\n4 - Sair')
            print ('__'*30)
            option = numeric_option(1,4)
            self.option = option

    def reading_store(self):
        while True:
            self.principal_menu() # '1 - Estoque\n2 - Cadastro de cliente\n3 - Vender Produto\n4 - Sair
            if self.option == 1:
                self.stock.principal_stock_menu()
            elif self.option == 2:
                self.cliente_manager.client_register()
            elif self.option == 3:
                self.cliente_manager.sale_menu()
            elif self.option == 4:
                self.bot.close_connetion()
                exit()


















