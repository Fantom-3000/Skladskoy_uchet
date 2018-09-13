"""
Created on Tue Aug 21 20:29:50 2018

@author: Fantom-3000
http://4pda.ru/forum/index.php?showuser=6015251
"""

class TransactionTabel():
      def __init__(self):
            # Параметры таблицы
            self.tabel_width = 85

            # Параметры колонок таблицы "Транзакции"
            self.date = 10
            self.type = 7
            self.product_name = 27
            self.unit_name = 10
            self.unit_price = 8
            self.amount = 7
            self.total = 10

class ProductTabel():
      def __init__(self):
            # Параметры таблицы
            self.tabel_width = 85

            # Ширина колонок таблицы "Справочник материалов"
            self.card_number = 9
            self.product_name = 43
            self.unit_name = 10
            self.unit_price = 8
            self.balance = 11
