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
            function.data_print(data)
            menu_view_transactions()
     
        # Вывод транзакций по категории "Расход"
        elif sel == '2':
            os.system(os_clear)
            sql = sql_start + """'Расход'""" + sql_end   
            cursor.execute(sql)
            data = cursor.fetchall()
            function.data_print(data)
            menu_view_transactions()

        # Вывод транзакций по категории "Перемещения"
        elif sel == '3':
            os.system(os_clear)
            sql = sql_start + """'Перемещ'""" + sql_end
            cursor.execute(sql)
            data = cursor.fetchall()
            function.data_print(data)
            menu_view_transactions()
