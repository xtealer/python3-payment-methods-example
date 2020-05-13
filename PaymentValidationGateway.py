from os import system, name
import time
import sys


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


class PaymentValidationGateway:
    def __init__(self):
        self.monto_total = 0

    def auth(self):
        return 'auth'

    def capture(self):
        return 'capture'

    def sale(self):
        return 'sale'

    def do_sale(self, *args):
        # argsv receives an arbitrary number of parameters in form of an array
        # more info at: https://book.pythontips.com/en/latest/args_and_kwargs.html
        if args[0].t_trans.lower() == "auth":
            tipo_trans = self.auth()
            print(tipo_trans)
        elif args[0].t_trans.lower() == "capture":
            tipo_trans = self.capture()
            print(tipo_trans)
        elif args[0].t_trans.lower() == "sale":
            tipo_trans = self.sale()
            print(tipo_trans)
        else:
            return 4

        # set card type
        if args[0].numero_tarjeta[0] == '4':
            args[0].tipo_tarjeta = "Visa"
        elif args[0].numero_tarjeta[0] == '5':
            args[0].tipo_tarjeta = "Master Card"
        elif args[0].numero_tarjeta[0] == '6':
            args[0].tipo_tarjeta = "American Express"
        else:
            return 5

        # out of range sale amount
        if args[0].monto < 1 or args[0].monto > 150000.00:
            return 6
