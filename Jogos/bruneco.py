from turtle import clear
from colorama import Fore, Back, Style

def jogar():

    print("*********************************")
    print("Bem vindo ao jogo do Bruneco!")
    print("*********************************")

    palavra_secreta = "teste"
    letras_acertadas = ["_" for letra in palavra_secreta]
    
    palavra_secreta = palavra_secreta.upper()

    acertou = False
    perdeu = False
    erros = 0

    gabarito_num = []
    gabarito_letra = []

    while(not perdeu and not acertou):
#restringir o tamanho do chute para 5 letras
        chute = input("Qual a palavra com 5 letras?")
        chute = chute.strip().upper()

        gabarito_letra.append(chute)

        index_chute = 0
        gabarito_tentativa = []
        for letra in chute:
            if letra == palavra_secreta[index_chute]:
                gabarito_tentativa.append(2)
            elif letra in palavra_secreta:
                gabarito_tentativa.append(1)
            else:
                gabarito_tentativa.append(0)
            index_chute += 1
        gabarito_num.append(gabarito_tentativa)
        acertou = chute == palavra_secreta
        perdeu = erros == 4

        erros += 1

#colocar final diferente para quando ganha e quando perde

        for lista in range(len(gabarito_num)):
            for letra in range(len(chute)):
                if gabarito_num[lista][letra] == 2:
                    print(Fore.BLACK + Back.GREEN + gabarito_letra[lista][letra] + Style.RESET_ALL, end = "")
                elif gabarito_num[lista][letra] == 1:
                    print(Fore.BLACK + Back.YELLOW + gabarito_letra[lista][letra] + Style.RESET_ALL, end = "")
                else:
                    print(Fore.BLACK + Back.RED + gabarito_letra[lista][letra] + Style.RESET_ALL, end = "")
            print("")

    print("*********************************")
    print("Fim de jogo!")
    print("*********************************")

if(__name__ == "__main__"):
    jogar()
