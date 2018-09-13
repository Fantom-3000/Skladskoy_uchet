"""
Created on Tue Aug 21 20:29:50 2018

@author: Fantom-3000
http://4pda.ru/forum/index.php?showuser=6015251
"""

import time
from settings import TransactionTabel, ProductTabel

# Конвертирование отпечатка даты в читаемый вид
def operation_date(unix_time):
    operation_date = time.strftime("%d.%m.%Y", time.localtime(unix_time))
    return operation_date

# Вывод данных по транзвкциям
def data_print(data):
    col = TransactionTabel()
    line_down() # ┌──────────┐
    print('│Дата запроса: ' +
          str(operation_date(time.time()).ljust(col.tabel_width-14, ' '))+'│')
    line_transaction_down() # ├──┬───┬───┤
    print('│'+'Дата'.center(col.date, ' ')+'│'+
          'Тип'.center(col.type, ' ')+'│'+
          'Наименование материала'.center(col.product_name, ' ')+'│'+
          'Ед.изм.'.center(col.unit_name, ' ')+'│'+
          'За ед.'.center(col.unit_price, ' ')+'│'+
          'Кол-во'.center(col.amount, ' ')+'│'+
          'Сумма'.center(col.total, ' ')+'│')
    line_transaction_center() # ├───┼───┼───┤

    for data_list in data:
        transaction_date = operation_date(data_list[0])
        transaction_type = data_list[1]
        product_name = data_list[2]
        unit_name = data_list[3]
        unit_price = data_list[4]
        amount = data_list[5]
        # description = data_list[6]
        total = unit_price * amount

        print('│'+str(transaction_date.ljust(col.date, ' '))+'│'+
              transaction_type.ljust(col.type, ' ')+'│'+
              product_name.ljust(col.product_name, ' ')+'│'+
              unit_name.center(col.unit_name, ' ')+'│'+
              str(unit_price).rjust(col.unit_price, ' ')+'│'+
              str(amount).rjust(col.amount, ' ')+'│'+
              str(total).rjust(col.total, ' ')+'│')
    line_transaction_up() # └──┴──┴──┘

# Добавление новой транзакции
def new_transaction():
    transaction_date = time.time()
    transaction_type = input('Тип транзакции --> ')
    product_name = input('Наименование материала --> ')
    unit_name = input('Единица измерения --> ')
    unit_price = float(input('Цена за единицу --> '))
    amount = float(input('Количество --> '))
    description = input('Назначение -->')

    print(transaction_date)

# ┌───────┐
def line_down():
    col = TransactionTabel()
    print('┌'+''.ljust(col.tabel_width, '─')+'┐')

# ├───────┤
def line_center():
    col = TransactionTabel()
    print('├'+''.ljust(col.tabel_width, '─')+'┤')

# └───────┘
def line_up():
    col = TransactionTabel()
    print('└'+''.ljust(col.tabel_width, '─')+'┘')

# ├──┬──┬──┤
def line_transaction_down():
    col = TransactionTabel()
    print('├'+''.ljust(col.date, '─')+'┬'+
          ''.ljust(col.type, '─')+'┬'+
          ''.ljust(col.product_name, '─')+'┬'+
          ''.ljust(col.unit_name, '─')+'┬'+
          ''.ljust(col.unit_price, '─')+'┬'+
          ''.ljust(col.amount, '─')+'┬'+
          ''.ljust(col.total, '─')+'┤')

# ├──┼──┼──┤
def line_transaction_center():
    col = TransactionTabel()
    print('├'+''.ljust(col.date, '─')+'┼'+
          ''.ljust(col.type, '─')+'┼'+
          ''.ljust(col.product_name, '─')+'┼'+
          ''.ljust(col.unit_name, '─')+'┼'+
          ''.ljust(col.unit_price, '─')+'┼'+
          ''.ljust(col.amount, '─')+'┼'+
          ''.ljust(col.total, '─')+'┤')

# └──┴──┴──┘
def line_transaction_up():
    col = TransactionTabel()
    print('└'+''.ljust(col.date, '─')+'┴'+
          ''.ljust(col.type, '─')+'┴'+
          ''.ljust(col.product_name, '─')+'┴'+
          ''.ljust(col.unit_name, '─')+'┴'+
          ''.ljust(col.unit_price, '─')+'┴'+
          ''.ljust(col.amount, '─')+'┴'+
          ''.ljust(col.total, '─')+'┘')

# ┌──┬──┬──┐
def line_product_down():
    col = ProductTabel()
    print('┌' + ''.ljust(col.card_number, '─') + '┬' +
          ''.ljust(col.product_name, '─') + '┬' +
          ''.ljust(col.unit_name, '─')+ '┬' +
          ''.ljust(col.unit_price, '─') + '┐')

# └──┴──┴──┘
def line_product_up():
    col = ProductTabel()
    print('└'+''.ljust(col.card_number, '─')+'┴'+
          ''.ljust(col.product_name, '─')+'┴'+
          ''.ljust(col.unit_name, '─')+'┴'+
          ''.ljust(col.unit_price, '─')+'┴'+
          ''.ljust(col.balance, '─')+'┘')

# ├──┬──┬──┤
def line_product_down_2():
    col = ProductTabel()
    print('├'+''.ljust(col.card_number, '─')+'┬'+
          ''.ljust(col.product_name, '─')+'┬'+
          ''.ljust(col.unit_name, '─')+'┬'+
          ''.ljust(col.unit_price, '─')+'┬'+
          ''.ljust(col.balance, '─')+'┤')

# ├──┼──┼──┤
def line_product_center():
    col = ProductTabel()
    print('├'+''.ljust(col.card_number, '─') + '┼' +
          ''.ljust(col.product_name, '─') + '┼' +
          ''.ljust(col.unit_name, '─') + '┼' +
          ''.ljust(col.unit_price, '─') + '┼' +
          ''.ljust(col.balance, '─') + '┤')

'''# Вывод списка материалов
def products_list(data):
    col = ProductTabel()
    line_down() # ┌───────┐
    print('│'+'Дата запроса: ' + 
          str(operation_date(time.time()).ljust(col.tabel_width-14, ' ')) + '│')
    line_product_down_2() # ├──┬──┬──┤
    print('│'+'Инв. ном.'.center(col.card_number, ' ') + '│' +
          'Наименование материала'.center(col.product_name, ' ') + '│' +
          'Ед. изм.'.center(col.unit_name, ' ') + '│' +
          'За ед.'.center(col.unit_price, ' ')+'│'+
          'Остаток'.center(col.balance, ' ')+'│')
    line_product_center() # ├──┼──┼──┤
    balance = '0.0'
    for data_list in data:
        card_number = data_list[0]
        product_name = data_list[1]
        unit_name = str(data_list[2])
        unit_price = str(data_list[3])
        print('│'+card_number.rjust(col.card_number, ' ') + '│' +
              product_name.ljust(col.product_name, ' ') + '│' +
              unit_name.center(col.unit_name, ' ') + '│' +
              unit_price.rjust(col.unit_price, ' ') + '│' +
              balance.rjust(col.balance, ' ') + '│')
    line_product_up() # └──┴──┴──┘
'''