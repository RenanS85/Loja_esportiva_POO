def initial_interface(txt):
    print('--' * 30)
    print(txt.upper().strip().center(60))
    print('--' * 30)


def basic_interface(txt):
    print(' ')
    text = txt.upper().strip()
    print(text.center(60))
    print('--' * 30)


def numeric_option( min, max):
    txt = 'DIGITE A OPÇÂO: '
    while True:
        option = read_int(f'{txt:>38}')
        if option < min or option > max:
            print('\033[31mErro - DIGITE UMA OPÇÃO VÁLIDA\033[m')
        else:
            break
    return option

def read_int(n):
    while True:
            try:
                number = int(input(n))
            except (TypeError,ValueError):
                print ('\033[31mErro - DIGITE UMA OPÇÃO VÁLIDA\033[m')
                continue
            else:
                return number


def read_price(txt):
    while True:
        try:
            price = input(txt).replace(',','.').strip()
            price_float = float(price)
        except (TypeError, ValueError):
            print('\033[31mErro - DIGITE UMA OPÇÃO VÁLIDA\033[m')
            continue
        else:
            print ('Preço validado')
            return price_float



def validation_yes_not_answer(target_answer):
    target = target_answer
    while True:
        if target != 'S' and target != 'N':
            print('\033[31mErro - DIGITE UMA OPÇÃO VÁLIDA\033[m')
            target = input ('DIGITE A OPÇÂO [S/N]: '.center(60)).upper().strip()
        else:
            break
    return target

def yes_or_not_option(txt_for_yes_not_option):
    print (txt_for_yes_not_option)
    pick_yes_or_not = input ('DIGITE A OPÇÂO [S/N]: ').upper().strip()
    validation = validation_yes_not_answer(pick_yes_or_not)
    return validation

def save_alterations_yes_or_not():
     apply = yes_or_not_option('Deseja aplicar as alterações feitas - (S - sim | N - não):')
     return apply


def back_previus_menu():
   yes_or_not_option('Voltar para o menu anterior?: ')



def validation(target_answer):
    target = target_answer
    while True:
        try:
            target = target_answer
        except target != 'S' and target != 'N':
            print('\033[31mErro - DIGITE UMA OPÇÃO VÁLIDA\033[m')
            continue
        else:
            break
    return target

def register_cpf():
    while True:
        cpf = input('CPF: ').strip().replace('.','').replace('-','')
        numeric = cpf.isnumeric()
        if not numeric:
            print('\033[31mErro - DIGITE UM CPF VÁLIDO\033[m')
            continue
        elif len(cpf) != 11:
            print('\033[31mErro - DIGITE UM CPF VÁLIDO\033[m')
            continue
        else:
            break
    return cpf

def register_cellphone():
    while True:
        cellphone = input('Celular: ').strip().replace('(', '').replace(')', '').replace('-', '')
        numeric = cellphone.isnumeric()
        if not numeric:
            print('\033[31mErro - DIGITE UM CPF VÁLIDO\033[m')
            continue
        if cellphone[0] == '0':
            a = ' '.join(cellphone)
            list = a.split()
            list.__delitem__(0)
            s=''
            for n in list:
                s+=n
            cellphone = s
        if len(cellphone) != 11:
            print('\033[31mErro - DIGITE UM CPF VÁLIDO\033[m')
            continue
        return cellphone
























