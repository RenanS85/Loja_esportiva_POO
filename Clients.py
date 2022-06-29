from I_SqliteBot import *
from J_uteis import *
from F_Product import *
from G_Product_manager import *


class Client:
    def __init__(self, name,cpf,cellphone=None,email=None):
        self.name = name
        self.cpf = cpf
        self.cellphone = cellphone
        self.email = email

class ClientManager:
    connection_name = 'LojaDoRenan.db'
    table_cliente = 'Clientes'
    connection = None
    sql_bot = SqlBot()
    product_manager = Product_manager()


    def client_register(self,register_for_sell=False):
        while True:
            initial_interface('cadastro de cliente')
            if not self.connection:
                self.connection = self.sql_bot.create_connetion(self.connection_name)
            name = input('Nome: ')
            cpf = register_cpf()
            cellphone = register_cellphone()
            email = input('E-mail: ')
            client_object = Client(name,cpf,cellphone,email)
            dic = client_object.__dict__
            print (dic)
            print('Você esta cadastrando:')
            print (f'Nome: {dic["name"]}\nCPF: {dic["cpf"]}\n'
                   f'Celular: {dic["cellphone"]}\nE-mail {dic["email"]}')
            certain = yes_or_not_option('Adicionar Cliente?')
            if certain == 'S':
                cur = self.connection.cursor()
                cur.execute (f'''insert into Clientes values 
                (null,"{dic["name"]}", "{dic["cpf"]}", "{dic["cellphone"]}","{dic["email"]}");''')
                self.connection.commit()
                cur.execute(f'''select * from Clientes where cpf = {dic["cpf"]}''')
                result = cur.fetchall()
                print (result)
            else:
                break
            if not register_for_sell:
                do_again = yes_or_not_option('Cadastrar mais clientes: ')
                if do_again == 'S':
                    continue
            else:
                break
        if register_for_sell:
            cur = self.connection.cursor()
            cur.execute(f''' select id from Clientes where cpf = {dic["cpf"]}''')
            result = cur.fetchone()
            print('Você irá vender para:')
            print(f'Nome: {dic["name"]}\nCPF: {dic["cpf"]}\n'
                  f'Celular: {dic["cellphone"]}\nE-mail {dic["email"]}')
            return result[0]

    def sale_menu(self):
        while True:
            initial_interface('menu de vendas')
            print ('1 - Vender para cliente cadastrado\n2 - Cadastrar novo cliente\n3 - Voltar')
            option = numeric_option(1,3)
            self.option = option
            if self.option == 1:
                initial_interface('filtrar cliente por:')
                print('1 - Nome\n2 - CPF\n3 - Voltar')
                option=numeric_option(1,3)
                self.option = option
                if self.option == 1:
                    self.client_filter(filter_by_name=True)
                    cliente_id = read_int('ID do cliente para venda: ')
                    self.sell_product_for_client(cliente_id)
                elif self.option == 2:
                    cliente_id = self.client_filter(filter_by_cpf=True)
                    self.sell_product_for_client(cliente_id)
            elif self.option == 2:
                client_id = self.client_register(register_for_sell=True)
                self.sell_product_for_client(client_id)
            elif self.option == 3:
                break



    def client_filter(self,filter_by_cpf=False,filter_by_name=False):
        initial_interface('filtro de clientes para venda de produtos')
        if not self.connection:
            self.connection = self.sql_bot.create_connetion(self.connection_name)
            if filter_by_cpf:
                cpf = input('Cpf: ')
                cur = self.connection.cursor()
                cur.execute(f''' select * from Clientes where cpf like "{cpf}%"''')
                result = cur.fetchall()
                for client in result:
                    print(f'ID: {client[0]}\nNome: {client[1]}\nCPF: {client[2]}\n'
                          f'Celular: {client[3]}\nE-mail {client[4]}')
                return result[0][0]
            if filter_by_name:
                name = input('Nome: ')
                cur = self.connection.cursor()
                cur.execute(f''' select * from Clientes where nome like "{name}%"''')
                result = cur.fetchall()
                for client in result:
                    print(f'ID: {client[0]}\nNome: {client[1]}\nCPF: {client[2]}\n'
                          f'Celular: {client[3]}\nE-mail {client[4]}')


    def sell_product_for_client(self,client_id):
        product_list = []
        while True:
            self.product_manager.product_filter_menu()
            id_product = read_int('ID do produto a vender: ')
            amount_product = read_int('Quantidade: ')
            if not self.connection:
                self.connection = self.sql_bot.create_connetion(self.connection_name)
            cur=self.connection.cursor()
            cur.execute(f'''select nome, preco from Produtos where id = {id_product}''')
            result = cur.fetchone()
            print('Voce irá adicionar ao carrinho:')
            price = result[1]
            total_price = price * amount_product
            product_name = result[0]
            print (f'Produto: {product_name}\nPreço total: R${total_price:.2f}')
            certain = yes_or_not_option('Adicionar ao carrinho?')
            if certain == 'S':
                prod_dic = {'client_id': client_id,'product_id':id_product,'product_name':product_name,
                            'amount': amount_product,'price':price,'total_price':total_price}
                product_list.append(prod_dic)
            do_again = yes_or_not_option('Adicionar mais produtos ao carrinho?')
            if do_again == 'S':
                continue
            else:
                break
        print (f'{"Produto":^20}{"Quantidade":^20}{"Preço":^20}{"Total":^20}')
        total_order=0
        for dic in product_list:
            print (f'{dic["product_name"]:^20}{dic["amount"]:^20}{dic["price"]:^20}{dic["total_price"]:^20}')
            total_order+=dic['total_price']
        print(f'VALOR TOTAL DO PEDIDO: R${total_order}')
        conclusion = yes_or_not_option('Concluir pedido?')
        if conclusion == 'S':
            if not self.connection:
                self.connection = self.sql_bot.create_connetion(self.connection_name)
            cur=self.connection.cursor()
            cur.execute(f'''insert into Pedido values 
        (null, {client_id}, {total_order}); ''')
            self.connection.commit()
        cur.execute('''select max (id) from Pedido;''')
        result = cur.fetchone()
        id_pedido = result[0]
        for dic in product_list:
            cur.execute(f'''insert into Pedido_Cliente values
            ({id_pedido}, {client_id}, {dic["product_id"]}, {dic["amount"]}, {dic["price"]},{dic["total_price"]});''')
            self.connection.commit()
            cur.execute(f'''update Produtos set quantidade = quantidade - {dic["amount"]} where id = {dic["product_id"]}''')
            self.connection.commit()








