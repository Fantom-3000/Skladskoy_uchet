"""
Created on Tue Aug 21 20:29:50 2018

@author: Fantom-3000
http://4pda.ru/forum/index.php?showuser=6015251
"""

import sqlite3 as lite
import re
import transactions
import new_transactions
import products
from os import system
from sys import platform

# Основное меню программы
def menu():
    print('1. Транзакции')
    print('2. Справочник материалов')
    print()
    print('q. Меню программы')
    print('m. Выход из программы')
    print()

con = lite.connect("sklad.db")
cursor = con.cursor()

if (platform == 'win32') or (platform == 'win64'):
    os_clear = 'cls'
else:
    os_clear = 'clear'

system(os_clear)
menu()

while True:
    sel = input("--> ")

    # [mMьЬ] - Меню программы
    if re.search(r"[mMьЬ]", sel):
        system(os_clear)
        menu()

    #[qQйЙ] - Выход из программы
    elif re.search(r"[qQйЙ]", sel):
        con.close()
        system(os_clear)
        break

    # [1] - подменю "Транзакции"
    elif sel == '1':
        system(os_clear)
        transactions.transaction(cursor, os_clear)
        menu()

    #[3] - подменю "Справочник материалов"
    elif sel =='2':
        system(os_clear)
        products.products(cursor, os_clear, con)
        menu()
