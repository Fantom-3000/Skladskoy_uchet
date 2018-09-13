"""
Created on Wed Aug 22 11:02:47 2018

@author: Fantom-3000
http://4pda.ru/forum/index.php?showuser=6015251

"""

import time
import function
import re
import os
from settings import ProductTabel

# Подменю "Справочник материалов"
def menu_products():
    print('1. Просмотр материалов')
    print('2. Редактирование материала')
    print('3. Добавление нового материала')
    print('4. Удаление материала')
    print()
    print('m. Меню программы')
    print('q. Предыдущее меню')
    print()

sql = """SELECT products.card_number, products.product_name, products.unit_name, products.unit_price
         FROM products
         ORDER BY products.card_number"""

sql_insert_product_start = 'INSERT INTO products (card_number, product_name, unit_name, unit_price) VALUES ('
sql_insert_product_end = ')'

def products(cursor, os_clear, con):
    menu_products()
    while True:
        sel = input("Справочник материалов --> ")
    
        # [mMьЬ] - Меню программы
        if re.search(r"[mMьЬ]", sel):
            os.system(os_clear)
            menu_products()

        #[qQйЙ] - Выход из подменю "Транзакции"
        elif re.search(r"[qQйЙ]", sel):
            os.system(os_clear)
            break

        # Просмотр материалов
        elif sel == '1':
            os.system(os_clear)
            cursor.execute(sql)
            data = cursor.fetchall()
            # function.products_list(data)

            # Вывод списка материалов
            col = ProductTabel()
            function.line_down() # ┌───────┐
            print('│'+'Дата запроса: ' + 
                  str(function.operation_date(time.time()).ljust(col.tabel_width-14, ' ')) + '│')
            function.line_product_down_2() # ├──┬──┬──┤
            print('│'+'Инв. ном.'.center(col.card_number, ' ') + '│' +
                  'Наименование материала'.center(col.product_name, ' ') + '│' +
                  'Ед. изм.'.center(col.unit_name, ' ') + '│' +
                  'За ед.'.center(col.unit_price, ' ')+'│'+
                  'Остаток'.center(col.balance, ' ')+'│')
            function.line_product_center() # ├──┼──┼──┤
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
            function.line_product_up() # └──┴──┴──┘
            menu_products()

        # Редактирование материала
        elif sel == '2':
            os.system(os_clear)
            card_number = input("Введите номер карты: --> ")
            
            print(card_number)

        # Добавление материала
        elif sel == '3':
            os.system(os_clear)
            card_number = input("Номер карты: --> ")
            product_name = input("Наименование материала: --> ")
            unit_name = input("Единица измерения: --> ")
            unit_price = input("Цена за единицу: --> ")
            sql_insert_product = """INSERT INTO products (card_number, product_name, unit_name, unit_price) VALUES (
                                 '"""+card_number+"', '"+product_name+"', '"+unit_name+"', "+unit_price+""")"""
            cursor.execute(sql_insert_product)
            con.commit()
            print(sql_insert_product)
