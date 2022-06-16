
class Conta:
    

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo um objeto {}".format(self))
        self.numero = numero #este objeto vai ter um atributo chamado número
        self.titular = titular
        self.saldo = saldo
        self.limite = limite



