
class Conta:
    

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo um objeto {}".format(self))
        self.__numero = numero #este objeto vai ter um atributo chamado número
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("O titular {} tem {} de saldo".format(self.__titular, self.__saldo))

    def deposita(self, valor):
        self.__saldo += valor
    
    def saca(self,valor):
        self.__saldo -= valor
    
    def transfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


