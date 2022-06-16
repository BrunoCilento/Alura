def cria_conta(numero, titular, saldo, limite):
    conta2 = {"numero": numero, "titular": titular, "saldo": saldo,"limite": limite}
    return conta2

def deposita(conta, valor):
    conta["saldo"] += valor 

def saca(conta, valor):
    conta["saldo"] -= valor

def extrato(conta):
    print("Slado é {}".format(conta["saldo"]))
