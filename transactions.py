"""
Created on Wed Aug 22 11:02:47 2018

@author: Fantom-3000
http://4pda.ru/forum/index.php?showuser=6015251

Модуль просмотра транзакций
"""
import time
import function
import re
import os
from settings import TransactionTabel

# Подменю "Просмотр транзакций"
def menu_view_transactions():
    print('1. Приход')
    print('2. Расход')
    print('3. Перемещение')
    print('4. Редактирование транзакции')
    print()
    print('m. Меню программы')
    print('q. Предыдущее меню')
    print()

sql_start = """SELECT transactions.transaction_date, transactions.transaction_type,
                      products.product_name, products.card_number, 
                      products.unit_price, transactions.amount, transactions.description
               FROM transactions, products
               WHERE (transactions.id_product=products.id)
                   AND (transactions.transaction_type="""
sql_end = """)ORDER BY transactions.transaction_date"""

# Вывод данных по транзвкциям
def data_print(data):
    col = TransactionTabel()
    function.line_down() # ┌──────────┐
    print('│Дата запроса: ' +
          str(function.operation_date(time.time()).ljust(col.tabel_width-14, ' '))+'│')
    function.line_transaction_down() # ├──┬───┬───┤
    print('│'+'Дата'.center(col.date, ' ')+'│'+
          'Тип'.center(col.type, ' ')+'│'+
          'Наименование материала'.center(col.product_name, ' ')+'│'+
          'Ед.изм.'.center(col.unit_name, ' ')+'│'+
          'За ед.'.center(col.unit_price, ' ')+'│'+
          'Кол-во'.center(col.amount, ' ')+'│'+
          'Сумма'.center(col.total, ' ')+'│')
    function.line_transaction_center() # ├───┼───┼───┤

    for data_list in data:
        transaction_date = function.operation_date(data_list[0])
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
    function.line_transaction_up() # └──┴──┴──┘

def view_transactions(cursor, os_clear):
    menu_view_transactions()
    while True:
        sel = input("Просмотр транзакции --> ")
    
        # [mMьЬ] - Меню программы
        if re.search(r"[mMьЬ]", sel):
            os.system(os_clear)
            menu_view_transactions()

        #[qQйЙ] - Выход из подменю "Транзакции"
        elif re.search(r"[qQйЙ]", sel):
            os.system(os_clear)
            break

        # Вывод транзакций по категории "Приход"
        elif sel == '1':
            os.system(os_clear)
            sql = sql_start + """'Приход'""" + sql_end            
            cursor.execute(sql)
            data = cursor.fetchall()
            data_print(data)
            menu_view_transactions()
     
        # Вывод транзакций по категории "Расход"
        elif sel == '2':
            os.system(os_clear)
            sql = sql_start + """'Расход'""" + sql_end   
            cursor.execute(sql)
            data = cursor.fetchall()
            data_print(data)
            menu_view_transactions()

        # Вывод транзакций по категории "Перемещения"
        elif sel == '3':
            os.system(os_clear)
            sql = sql_start + """'Перемещ'""" + sql_end
            cursor.execute(sql)
            data = cursor.fetchall()
            data_print(data)
            menu_view_transactions()
