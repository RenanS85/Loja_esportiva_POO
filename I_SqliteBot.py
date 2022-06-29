import J_uteis
import sqlite3
class SqlBot:

    connection_name = 'LojaDoRenan.db'
    def __init__(self):
        self.connection = None

    def bot_connection_name(self):
        return self.connection

    def create_connetion(self,connection_name):
            try:
                self.connection = sqlite3.connect(connection_name)
            except sqlite3.Error as er:
                print(er)
            else:
                print('conexão estabelecida')
            return self.connection

    def close_connetion(self):
        try:
            self.connection.close
        except sqlite3.Error as er:
            print(er)
        else:
            print ('Conexão encerrada')
            self.connection = None

    def bot_sql(self,sql):
        if self.connection:
            try:
                cur = self.connection.cursor()
                cur.execute(sql)
            except sqlite3.Error as er:
                print(er)
            else:
                self.connection.commit()

    def select_all_table(self, title_table,show_result = False):
        if not self.connection:
            self.create_connetion(self.connection_name)
        try:
            cur = self.connection.cursor()
            cur.execute(f'''select * from '{title_table}';''')
        except sqlite3.Error as er:
            print(er)
        else:
            result = cur.fetchall()
            if result == []:
                empty = True
                return empty
            else:
                if show_result:
                    print('id'.center(30),'Nome'.center(30))
                    for c in result:
                        id = c[0]
                        name = c[1]
                        print(f'{id:^30}| {name:^30}')

    def insert_category_or_supplier_data(self, table_title, txt_data_name):
        if not self.connection:
            self.create_connetion(self.connection_name)
        data_name = input(txt_data_name)
        certain = J_uteis.save_alterations_yes_or_not()
        if certain == 'S':
            try:
                cur = self.connection.cursor()
                cur.execute (f'''
                      insert into '{table_title}' values 
                      (null,'{data_name}');''')
                self.connection.commit()
            except sqlite3.Error as er:
                print(er)
            else:
                cur.execute(f'''select * from "{table_title}" where nome = "{data_name}";''')
                print('Visualização dos dados inseridos:')
                result = cur.fetchall()
                print('id'.center(30), 'Nome'.center(30))
                for c in result:
                    id = c[0]
                    name = c[1]
                    print(f'{id:^30}| {data_name:^30}')
        return data_name



    def select_data_by_name(self, table_title, target_column_title, txt_object_name):
        if not self.connection:
            self.create_connetion(self.connection_name)
        object = input(txt_object_name)
        try:
            cur = self.connection.cursor()
            cur.execute(f'''select * from "{table_title}" where "{target_column_title}" like "{object}%";''')
        except sqlite3.Error as er:
            print(er)
        else:
            result = cur.fetchall()
            print('id'.center(30),'Nome'.center(30))
            for c in result:
                id = c[0]
                name = c[1]
                print(f'{id:^30}| {name:^30}')

    def select_data_by_id(self, table_title, txt_object_id):
        if not self.connection:
            self.create_connetion(self.connection_name)
        target_id = J_uteis.read_int(txt_object_id)
        try:
            cur = self.connection.cursor()
            cur.execute(f'''select * from "{table_title}" where id = {target_id};''')
        except sqlite3.Error as er:
            print(er)
        else:
            result = cur.fetchall()
            for c in result:
                target_id = c[0]
                name = c[1]
                print(f'{target_id:^30}| {name:^30}')


    def update_stock_data(self, table_title, txt_target_id, txt_new_name_title):
        if not self.connection:
            self.create_connetion(self.connection_name)
        target_id = J_uteis.read_int(txt_target_id)
        name = input(txt_new_name_title)
        certain = J_uteis.save_alterations_yes_or_not()
        if certain == 'S':
            try:
                cur = self.connection.cursor()
                cur.execute(f'''update "{table_title}" set nome = '{name}' where id = {target_id};''')
                self.connection.commit()
            except sqlite3.Error as er:
                print(er)
            else:
                cur.execute(f'''select * from "{table_title}"F where id = {target_id};''')
                print ('Visualização da categoria alterada')
                result = cur.fetchall()
                print('id'.center(30), 'Nome'.center(30))
                for c in result:
                    txt_target_id = c[0]
                    name = c[1]
                    print(f'{target_id:^30}| {name:^30}')


    def delete_one_row (self, table_title, txt_target_id, delete_product_category=False, delete_product_supplier = False):
        if not self.connection:
            self.create_connetion(self.connection_name)
        target_id = J_uteis.read_int(txt_target_id)
        certain = J_uteis.save_alterations_yes_or_not()
        if certain == 'S':
            if delete_product_category:
                cur = self.connection.cursor()
                cur.execute(f'''update Produtos set id_categoria = null where id_categoria = {target_id};''')
                cur.execute(f'''delete from "{table_title}" where id = {target_id};''')
                self.connection.commit()
            elif delete_product_supplier:
                cur = self.connection.cursor()
                cur.execute(f'''update Produtos set id_fornecedor = null where id_fornecedor = {target_id};''')
                cur.execute(f'''delete from "{table_title}" where id = {target_id};''')
                self.connection.commit()
            else:
                cur = self.connection.cursor()
                cur.execute(f'''delete from "{table_title}" where id = {target_id};''')
                self.connection.commit()
            print('DELETADO COM SUCESSO!!')
            return target_id


    def delete_all_rows_from_a_table(self, table_title,delete_category=False,delete_supplier=False,delete_product=False):
        if not self.connection:
            self.create_connetion(self.connection_name)
        certain = J_uteis.yes_or_not_option('TEM CERTEZA QUE DESEJA DELETAR TODAS AS CATEGORIAS?')
        if certain == 'S':
            try:
                cur = self.connection.cursor()
                cur.execute(f'''delete from "{table_title}";''')
                self.connection.commit()
            except sqlite3.Error as er:
                print(er)
            else:
                if delete_category:
                    cur.execute(f'''UPDATE Produtos set id_categoria = null where id_categoria is not null;''')
                print('Todas as categorias deletadas com sucesso!')
                if delete_supplier:
                    cur.execute(f'''UPDATE Produtos set id_fornecedor = null where id_fornecedor is not null;''')
                    print('Todas os fornecedores deletados com sucesso!')
                if delete_product:
                    print('Todas os produtos deletados com sucesso!')
                self.connection.commit()




    def table_lenght(self,table_title):
        if not self.connection:
            self.create_connetion(self.connection_name)
        try:
            cur = self.connection.cursor()
            cur.execute(f'''select * from "{table_title}";''')
        except sqlite3.Error as er:
            print(er)
        else:
            result = cur.fetchall()
            lenght = len(result)
            return lenght















