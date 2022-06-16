import random






def jogar():

    imprime_mensagem_abertura()
    

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha o nível de dificuldade: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5


    for rodada in range(1, total_de_tentativas + 1):
        print(f"Tentativa {rodada} de {total_de_tentativas}")
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute_int = int(chute_str)

        if(chute_int < 1 or chute_int > 100):
            print("Você deve digitar um número entre 1 e 100!!")
            continue

        acertou = chute_int == numero_secreto
        maior = chute_int > numero_secreto
        menor = chute_int < numero_secreto

        if(acertou):
            print(f"Parabéns você acertou e fez {pontos} pontos :)")
            break
        else:
            if(rodada == total_de_tentativas):
                print(f"O número secreto era {numero_secreto}")
                break
            if(maior):
                print("Você errou para cima")
            elif(menor):
                print("Você errou para baixo")
        pontos_perdidos = abs(numero_secreto - chute_int)
        pontos = pontos - pontos_perdidos

    print("*********************************")
    print("Fim de jogo!")
    print("*********************************")


def imprime_mensagem_abertura():
    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")








if(__name__ == "__main__"):
    jogar()