from os import system, name
import time
import sys
from PaymentValidationGateway import PaymentValidationGateway
from typing import Type


# define native clear screen method
def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


# create payment validation reference
paymentValidationGateway = PaymentValidationGateway()


class Main:
    def __init__(self):
        self.dicct = {"Error": 500,
                      "message": "Esta no es una tarjeta permitida"}
        self.dicc = {"Error": 500,
                     "message": "Esto no es una transacción permitida"}
        self.montx = "Es monto no es permitido"
        self.resp = 's'
        self.t_trans = ""
        # pato
        self.transs = 0
        self.cadena = ""
        self.inicial_aux = ""
        self.monto = 0
        self.aux = 0
        self.tipo_tarjeta = ""
        self.numero_tarjeta = ""

    def transaccion(self):
        print("""
================================
      Tipo de transacción       
================================""")
        self.t_trans = input("---> ")

        # need to ask for card number if sale selected and payment method is card
        self.numero_tarjeta = "5555 5555 5555 5555"
        self.monto = 100

        # payment validation
        paymentValidationGateway.do_sale(self)

        print(f'''
last value of class variables:
sale: {self.monto}
transaction: {self.t_trans}
card number: {self.numero_tarjeta}
card provider: {self.tipo_tarjeta}
''')


# create class instance
main = Main()

# program entry point
main.transaccion()
