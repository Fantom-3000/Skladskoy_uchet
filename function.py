"""
Created on Tue Aug 21 20:29:50 2018

@author: Fantom-3000
http://4pda.ru/forum/index.php?showuser=6015251
"""

import time
from settings import ColWidth

# Конвертирование отпечатка даты в читаемый вид
def operation_date(unix_time):
    operation_date = time.strftime("%d.%m.%Y", time.localtime(unix_time))
    return operation_date

# Вывод данных по транзвкциям
def data_print(data):
      transaction_tabel = ColWidth()
      line_down() # ┌──────────┐
      print('│Дата запроса: ' +
            str(operation_date(time.time()).ljust(transaction_tabel.tabel_width-14, ' '))+'│')
      line_transaction_down() # ├──┬───┬───┤
      print('│'+'Дата'.center(transaction_tabel.date, ' ')+'│'+
            'Тип'.center(transaction_tabel.type, ' ')+'│'+
            'Наименование материала'.center(transaction_tabel.product_name, ' ')+'│'+
            'Ед.изм.'.center(transaction_tabel.unit_name, ' ')+'│'+
            'За ед.'.center(transaction_tabel.unit_price, ' ')+'│'+
            'Кол-во'.center(transaction_tabel.amount, ' ')+'│'+
            'Сумма'.center(transaction_tabel.total, ' ')+'│')
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

            print('│'+str(transaction_date.ljust(transaction_tabel.date, ' '))+'│'+
                  transaction_type.ljust(transaction_tabel.type, ' ')+'│'+
                  product_name.ljust(transaction_tabel.product_name, ' ')+'│'+
                  unit_name.center(transaction_tabel.unit_name, ' ')+'│'+
                  str(unit_price).rjust(transaction_tabel.unit_price, ' ')+'│'+
                  str(amount).rjust(transaction_tabel.amount, ' ')+'│'+
                  str(total).rjust(transaction_tabel.total, ' ')+'│')
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
      col = ColWidth()
      print('┌'+''.ljust(col.tabel_width, '─')+'┐')

# ├───────┤
def line_center():
      col = ColWidth()
      print('├'+''.ljust(col.tabel_width, '─')+'┤')

# └───────┘
def line_up():
      col = ColWidth()
      print('└'+''.ljust(col.tabel_width, '─')+'┘')

# ├──┬──┬──┤
def line_transaction_down():
      col = ColWidth()
      print('├'+''.ljust(col.date, '─')+'┬'+
            ''.ljust(col.type, '─')+'┬'+
            ''.ljust(col.product_name, '─')+'┬'+
            ''.ljust(col.unit_name, '─')+'┬'+
            ''.ljust(col.unit_price, '─')+'┬'+
            ''.ljust(col.amount, '─')+'┬'+
            ''.ljust(col.total, '─')+'┤')

# ├──┼──┼──┤
def line_transaction_center():
      col = ColWidth()
      print('├'+''.ljust(col.date, '─')+'┼'+
            ''.ljust(col.type, '─')+'┼'+
            ''.ljust(col.product_name, '─')+'┼'+
            ''.ljust(col.unit_name, '─')+'┼'+
            ''.ljust(col.unit_price, '─')+'┼'+
            ''.ljust(col.amount, '─')+'┼'+
            ''.ljust(col.total, '─')+'┤')

# └──┴──┴──┘
def line_transaction_up():
      col = ColWidth()
      print('└'+''.ljust(col.date, '─')+'┴'+
            ''.ljust(col.type, '─')+'┴'+
            ''.ljust(col.product_name, '─')+'┴'+
            ''.ljust(col.unit_name, '─')+'┴'+
            ''.ljust(col.unit_price, '─')+'┴'+
            ''.ljust(col.amount, '─')+'┴'+
            ''.ljust(col.total, '─')+'┘')

# ┌──┬──┬──┐
def line_product_down():
      col = ColWidth()
      print('┌' + ''.ljust(col.card_number, '─') + '┬' +
            ''.ljust(col.product_name + col.product_name_koef, '─') + '┬' +
            ''.ljust(col.unit_name, '─')+ '┬' +
            ''.ljust(col.unit_price, '─') + '┐')

# └──┴──┴──┘
def line_product_up():
      col = ColWidth()
      print('└'+''.ljust(col.card_number, '─')+'┴'+
            ''.ljust(col.product_name + col.product_name_koef, '─')+'┴'+
            ''.ljust(col.unit_name, '─')+'┴'+
            ''.ljust(col.unit_price, '─')+'┴'+
            ''.ljust(col.balance, '─')+'┘')

# ├──┬──┬──┤
def line_product_down_2():
      col = ColWidth()
      print('├'+''.ljust(col.card_number, '─')+'┬'+
            ''.ljust(col.product_name + col.product_name_koef, '─')+'┬'+
            ''.ljust(col.unit_name, '─')+'┬'+
            ''.ljust(col.unit_price, '─')+'┬'+
            ''.ljust(col.balance, '─')+'┤')

# ├──┼──┼──┤
def line_product_center():
      col = ColWidth()
      print('├'+''.ljust(col.card_number, '─') + '┼' +
            ''.ljust(col.product_name + col.product_name_koef, '─') + '┼' +
            ''.ljust(col.unit_name, '─') + '┼' +
            ''.ljust(col.unit_price, '─') + '┼' +
            ''.ljust(col.balance, '─') + '┤')

# Вывод списка материалов
def products_list(data):
      col = ColWidth()
      line_down() # ┌───────┐
      print('│'+'Дата запроса: ' + 
            str(operation_date(time.time()).ljust(col.tabel_width-14, ' ')) + '│')
      line_product_down_2() # ├──┬──┬──┤
      print('│'+'Инв. ном.'.center(col.card_number, ' ') + '│' +
            'Наименование материала'.center(col.product_name + col.product_name_koef, ' ') + '│' +
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
                  product_name.ljust(col.product_name + col.product_name_koef, ' ') + '│' +
                  unit_name.center(col.unit_name, ' ') + '│' +
                  unit_price.rjust(col.unit_price, ' ') + '│' +
                  balance.rjust(col.balance, ' ') + '│')
      line_product_up() # └──┴──┴──┘
