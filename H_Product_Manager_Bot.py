from G_Product_manager import *

class Product_Manager_Bot:

    connection_name = 'LojaDoRenan.db'
    table_product = 'Produtos'
    table_category = 'Categorias Produtos'
    table_supplier = 'Fornecedor'
    category_functions = Category()
    supplier_functions = Suppliers()
    sql_bot = SqlBot()
    connection = None

    def insert_product_new_new(self, product_dictionary,category_id,supplier_id):
        if not self.connection:
            self.connection = self.sql_bot.create_connetion(self.connection_name)
        print ('Vocè irá adicioar:'.center(60))
        cur = self.connection.cursor()
        cur.execute(f'''select cp.nome, f.nome 
        from "Categorias Produtos" cp, "Fornecedor" f
        where cp.id = {category_id} and f.id = {supplier_id};''')
        result = cur.fetchall()
        print(result)
        for key, value in product_dictionary.items():
            if key == 'category':
                value = result[0][0]
                print(key,'-->',value)
            elif key == 'supplier':
                value = result[0][1]
                print(key, '-->', value)
            else:
                print(key, '-->', value)
        certain = save_alterations_yes_or_not()
        if certain == 'S':
            try:
                cur = self.connection.cursor()
            except sqlite3.Error as er:
                print(er)
            else:
                cur.execute(f'''insert into Produtos values
                                (null,{category_id}, {supplier_id}, "{product_dictionary['name']}",
                                 {product_dictionary['price']}, {product_dictionary['amount']});''')
                self.connection.commit()
                print('Produto adicionado com sucesso!')

    def select_new_supplier_id(self, supplier_name):
        if not self.connection:
            self.connection = self.sql_bot.create_connetion(self.connection_name)
        cur = self.connection.cursor()
        cur.execute(f'''select id from Fornecedor where nome = "{supplier_name}";''')
        result = cur.fetchall()
        return result[0][0]

    def select_new_category_id(self,category):
        if not self.connection:
            self.connection = self.sql_bot.create_connetion(self.connection_name)
        cur = self.connection.cursor()
        cur.execute(f'''select id from "Categorias Produtos" where nome = "{category}";''')
        result = cur.fetchall()
        return result[0][0]

    def product_show_all(self,without_category=False, without_supplier=False, whithout_nothing=False):
        if not self.connection:
            self.connection = self.sql_bot.create_connetion(self.connection_name)

        complete = self.connection.cursor()
        complete.execute('''
        select p.id, p.nome, p.preco, p.quantidade, cp.nome as Categoria, f.nome as Fornecedor 
        from Produtos p, "Categorias Produtos" cp, Fornecedor f
        where p.id_categoria = cp.id and f.id = p.id_fornecedor;''')

        just_supplier = self.connection.cursor()
        just_supplier.execute('''SELECT p.id , p.nome ,p.preco , p.quantidade, f.nome as fornecedor
        from Produtos p, Fornecedor f
        where f.id = p.id_fornecedor;''')

        just_category = self.connection.cursor()
        just_category.execute('''select p.id , p.nome ,p.preco , p.quantidade, cp.nome as categoria
        from Produtos p , "Categorias Produtos" cp
        where cp.id = p.id_categoria;''')

        just_product = self.connection.cursor()
        just_product.execute('''select p.id , p.nome ,p.preco , p.quantidade
        from Produtos p ''')

        if without_category:
            result_just_supplier = just_supplier.fetchall()
            if result_just_supplier != []:
                result = result_just_supplier
                print('id'.center(25), 'Nome'.center(25), 'Preço'.center(25), 'Quantidade'.center(25),
                      'Categoria'.center(25), 'Fornecedor'.center(25))
                for product in result:
                    print(f'{product[0]:^25}|{product[1]:^25}|{product[2]:^25}|{product[3]:^25}|{"Sem categoria":^25}|{product[4]:^25}')
            else:
                print('Não há produtos sem categoria :)')
        elif without_supplier:
            result_just_category = just_category.fetchall()
            if result_just_category !=[]:
                result = result_just_category
                print('id'.center(25), 'Nome'.center(25), 'Preço'.center(25), 'Quantidade'.center(25),
                      'Categoria'.center(25), 'Fornecedor'.center(25))
                for product in result:
                    print(f'{product[0]:^25}|{product[1]:^25}|{product[2]:^25}|{product[3]:^25}|{product[4]:^25}|{"Sem fornecedor":^25}')
            else:
                print('Não há produtos sem fornecedor :)')
        elif whithout_nothing:
            result_just_product = just_product.fetchall()
            if result_just_product != []:
                result = result_just_product
                print('id'.center(25), 'Nome'.center(25), 'Preço'.center(25), 'Quantidade'.center(25),
                      'Categoria'.center(25), 'Fornecedor'.center(25))
                for product in result:
                    print(f'{product[0]:^25}|{product[1]:^25}|{product[2]:^25}|{product[3]:^25}|{"Sem categoria":^25}|{"Sem fornecedor":^25}')
            else:
                print('Não há produtos sem categoria e sem fornecedor :)')
        else:
            result_complete = complete.fetchall()
            result_just_supplier = just_supplier.fetchall()
            result_just_category = just_category.fetchall()
            result_just_product = just_product.fetchall()
            result = None
            if result_complete != []:
                result = result_complete
            elif result_just_supplier != []:
                result = result_just_supplier
            elif result_just_category != []:
                result = result_just_category
            elif result_just_product != []:
                result = result_just_product
            print('id'.center(25),'Nome'.center(25),'Preço'.center(25),'Quantidade'.center(25),'Categoria'.center(25),'Fornecedor'.center(25))
            for product in result:
                if result == result_complete:
                    print(f'{product[0]:^25}|{product[1]:^25}|{product[2]:^25}|{product[3]:^25}|{product[4]:^25}|{product[5]:^25}')
                elif result == result_just_supplier:
                    print(f'{product[0]:^25}|{product[1]:^25}|{product[2]:^25}|{product[3]:^25}|{"Sem categoria":^25}|{product[4]:^25}')
                elif result == result_just_category:
                    print(f'{product[0]:^25}|{product[1]:^25}|{product[2]:^25}|{product[3]:^25}|{product[4]:^25}|{"Sem fornecedor":^25}')
                elif result == result_just_product:
                    print(f'{product[0]:^25}|{product[1]:^25}|{product[2]:^25}|{product[3]:^25}|{"Sem categoria":^25}|{"Sem fornecedor":^25}')





    def select_product_by_name(self, txt_product_name):
        if not self.connection:
            self.connection = self.sql_bot.create_connetion(self.connection_name)
        product_name = input(txt_product_name)
        cur = self.connection.cursor()
        cur.execute(f''' 
select * from Produtos where nome like "{product_name}%";''')

    def select_product_by_id(self, txt_product_id):
        if not self.connection:
            self.connection = self.sql_bot.create_connetion(self.connection_name)
        product_id = input(txt_product_id)
        cur = self.connection.cursor()
        cur.execute(f''' 
select * from Produtos where id = {product_id};''')

    def select_product_by(self, by_product_name = False, by_prodduct_id = False, by_category = False, by_supplier = False):
        if not self.connection:
            self.connection = self.sql_bot.create_connetion(self.connection_name)
        if by_product_name:
            product_name = input ('Digite o nome do produto: ').strip()
            cur = self.connection.cursor()
            cur.execute(f'''
select p.id, p.nome, p.preco, p.quantidade, cp.nome as Categoria, f.nome as Fornecedor 
from Produtos p, "Categorias Produtos" cp, Fornecedor f 
where p.id_categoria = cp.id and f.id = p.id_fornecedor and p.nome LIKE "{product_name}%";''')
            result = cur.fetchall()
            for product in result:
                print(f'ID = {product[0]}\nNome = {product[1]}\nPreço = R${product[2]:.2f}\nQuantidade = {product[3]}'
                      f'\nCategoria = {product[4]}\nFornecedor = {product[5]}')
        if by_prodduct_id:
            product_id = input('ID do produto: ')
            cur = self.connection.cursor()
            cur.execute(f'''
select p.id, p.nome, p.preco, p.quantidade, cp.nome as Categoria, f.nome as Fornecedor 
from Produtos p, "Categorias Produtos" cp, Fornecedor f 
where p.id_categoria = cp.id and f.id = p.id_fornecedor and p.id = {product_id};''')
            result = cur.fetchall()
            for product in result:
                print(f'ID = {product[0]}\nNome = {product[1]}\nPreço = R${product[2]:.2f}\nQuantidade = {product[3]}'
                      f'\nCategoria = {product[4]}\nFornecedor = {product[5]}')
        if by_category:
            empty = self.sql_bot.select_all_table(self.table_category)
            if empty:
                print('Ops, não há categorias cadastradas')
            else:
                cur = self.connection.cursor()
                basic_interface('1 - Buscar produto por nome de categoria\n 2 - Buscar por ID de categoria\n3 - Voltar')
                option = numeric_option(1,3)
                if option == 1:
                    product_category = input('Nome Categoria: : ')
                    cur.execute(f'''
    select p.id, p.nome, p.preco, p.quantidade, cp.nome as Categoria, f.nome as Fornecedor 
    from Produtos p, "Categorias Produtos" cp, Fornecedor f 
    where p.id_categoria = cp.id and f.id = p.id_fornecedor and cp.nome like "{product_category}%";''')
                elif option == 2:
                    product_category = input('ID da categoria: ')
                    cur.execute(f'''
    select p.id, p.nome, p.preco, p.quantidade, cp.nome as Categoria, f.nome as Fornecedor 
    from Produtos p, "Categorias Produtos" cp, Fornecedor f 
    where p.id_categoria = cp.id and f.id = p.id_fornecedor and cp.id = {product_category};''')
                result = cur.fetchall()
                for product in result:
                    print(f'ID = {product[0]}\nNome = {product[1]}\nPreço = R${product[2]:.2f}\nQuantidade = {product[3]}'
                          f'\nCategoria = {product[4]}\nFornecedor = {product[5]}')
        if by_supplier:
            empty = self.sql_bot.select_all_table(self.table_category)
            if empty:
                print('Ops, não há fornecedores cadastrados')
            else:
                cur = self.connection.cursor()
                basic_interface('1 - Buscar produto por nome do fornecedor\n2 - Buscar produto por ID do fornecedor\n3 - Sair')
                option = numeric_option(1,3)
                if option == 1:
                    product_supplier = input('Nome fornecedor')
                    cur.execute(f'''
    select p.id, p.nome, p.preco, p.quantidade, cp.nome as Categoria, f.nome as Fornecedor 
    from Produtos p, "Categorias Produtos" cp, Fornecedor f 
    where p.id_categoria = cp.id and f.id = p.id_fornecedor and f.nome like "{product_supplier}%";''')
                elif option == 2:
                    product_supplier = input('ID do foencedor')
                    cur.execute(f'''
    select p.id, p.nome, p.preco, p.quantidade, cp.nome as Categoria, f.nome as Fornecedor 
    from Produtos p, "Categorias Produtos" cp, Fornecedor f 
    where p.id_categoria = cp.id and f.id = p.id_fornecedor and f.id = {product_supplier};''')
                result = cur.fetchall()
                for product in result:
                    print(f'ID = {product[0]}\nNome = {product[1]}\nPreço = R${product[2]:.2f}\nQuantidade = {product[3]}'
                          f'\nCategoria = {product[4]}\nFornecedor = {product[5]}')



    def simple_update_product (self, target_id, uptade_name = False, update_price = False, update_amount = False,
                        update_category = False, update_supplier = False):
        if not self.connection:
            self.connection = self.sql_bot.create_connetion(self.connection_name)
        if uptade_name:
            name = input('Novo nome do produto: ')
            cur = self.connection.cursor()
            cur.execute(f'''
update Produtos set nome = "{name}" where id = {target_id}''')
        if update_price:
            price = read_price('Novo preço do produto: ')
            cur = self.connection.cursor()
            cur.execute(f'''
    update Produtos set preco = "{price}" where id = {target_id}''')
        if update_amount:
            basic_interface('1 - Resetar quantidade\n2 - Adicionar quantidade\n3 - Subtrair quantidade ')
            option = numeric_option(1,2)
            if option == 1:
                amount = read_int('Nova quantidade do produto: ')
                cur = self.connection.cursor()
                cur.execute(f'''
            update Produtos set preco = "{amount}" where id = {target_id}''')
            elif option == 2:
                amount = read_int('Quantidade a adicionar: ')
                cur = self.connection.cursor()
                cur.execute(f'''update Produtos set quantidade = quantidade + {amount} where id = {target_id}''')
            elif option == 3:
                amount = read_int('Quantidade a subtrair: ')
                cur = self.connection.cursor()
                cur.execute(f'''update Produtos set quantidade = quantidade - {amount} where id = {target_id}''')
        if update_category:
           consult = self.category_functions.categories_consult_menu()
           new_category = read_int('ID da nova categoria: ')
           cur = self.connection.cursor()
           cur.execute(f'''update Produtos set id_categoria = {new_category} where id= {target_id}''')
        if update_supplier:
           self.supplier_functions.supplier_consult_menu()
           new_supplier = read_int('ID do novo fornecedor: ')
           cur = self.connection.cursor()
           cur.execute(f'''update Produtos set id_fornecedor = {new_supplier} where id= {target_id}''')
        self.connection.commit()

    def delete_all_products_without(self,without_category=False,without_supplier=False):
        if not self.connection:
            self.sql_bot.create_connetion(self.connection_name)
        if without_category:
            cur = self.connection.cursor()
            cur.execute(''' delete from Produtos where id_categoria is null''')
        if without_supplier:
            cur = self.connection.cursor()
            cur.execute(''' delete from Produtos where id_fornecedor is null''')
        self.connection.commit()



















