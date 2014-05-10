# -*-coding:Utf-8 -*

from decimal import *

__author__ = 'chatelain'

class Transaction:

    def __init__(self, id, label, value):
        self.id = id
        self.label = label
        self.value = Decimal(value)
