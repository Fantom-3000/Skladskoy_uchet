"""
Created on Wed Aug 22 11:02:47 2018

@author: Fantom-3000
http://4pda.ru/forum/index.php?showuser=6015251

"""
import time
import function
import re
import os

# Подменю "Добавить транзакцию"
def menu_new_transaction():
    print("""
1. Приход
2. Расход
3. Перемещение

m. Меню программы
q. Предыдущее меню
""")
                                                
def add_new_transaction(cursor, os_clear):
    menu_new_transaction()
    while True:
        sel = input("Добавление транзакции --> ")
    
        # [mMьЬ] - Меню программы
        if re.search(r"[mMьЬ]", sel):
            os.system(os_clear)
            menu_new_transaction()

        #[qQйЙ] - Выход из подменю "Транзакции"
        elif re.search(r"[qQйЙ]", sel):
            os.system(os_clear)
            break
