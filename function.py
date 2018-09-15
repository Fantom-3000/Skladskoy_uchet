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
