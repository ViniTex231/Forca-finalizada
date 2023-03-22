import os
from threading import Timer
from api import pegar_palavra


def visual():
    print('\033[31m-=' * 30)
    print('-=' * 10, "[ JOGO DA FORCA! ]", '-=' * 10)
    print('-=' * 30)
    print()
    apresentacao()


def apresentacao():
    tamanho_palavra = len(palavra_sorteada)
    print(f"\033[33m* A dica é:", dica_sorteada)
    print(f"* Quantidade de letras:", tamanho_palavra)
    print(f"* Você tem 20 segundos para completar a forca!")
    funcionamento(vida)


def funcionamento(vida):
    while True:
        print(f"* Sua vida é:", vida)
        for i in tracejado:
            print(i, end=' ')
        print('')
        tentativa = input("Digite a letra da sua tentativa: ").lower()
        tempo()
        if tentativa in letras_certas:
            print("Essa palavra ja foi digitada.")
        elif tentativa in letras_erradas:
            print("Essa palavra ja foi digitada.")
        elif len(tentativa) >= 2:
            print("Quantidade de letras incorreta, digite apenas 1 letra.")
        else:
            if tentativa not in palavra_sorteada:
                forca(vida)
                print("Essa letra não está na palavra sorteada :(")
                letras_erradas.append(tentativa)
                vida = perder_vida(vida)
            else:
                for i, char in enumerate(palavra_sorteada):
                    if tentativa == char:
                        letras_certas.append(tentativa)
                        tracejado.pop(i)
                        tracejado.insert(i, char)
                finaliza = finalizar_jogo()
                if finaliza:
                    break
            if perder_jogo(vida):
                break


def perder_vida(vida):
    vida = vida - 1
    return vida


def perder_jogo(vida):
    if vida == 0:
        print(f"A palavra era: {palavra_sorteada}")
        terminar_tempo("Suas vidas acabaram! 🙄")
        return True


def finalizar_jogo():
    if not "_" in tracejado:
        terminar_tempo("Parabens, você ganhou!! 😀")
        return True


def terminar_tempo(msg="\nO tempo acabou... 😥"):
    print(msg)
    print(f"A palavra era: {palavra_sorteada}")
    pid = os.getpid()
    os.kill(pid, -1)


def tempo():
    timer = Timer(20, terminar_tempo)
    timer.start()


def forca(vida):
    print("  _______     ")
    print(" |/      |    ")
    if vida == 7:
        print()
    elif vida == 6:
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")
    elif vida == 5:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")
    elif vida == 4:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")
    elif vida == 3:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")
    elif vida == 2:
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
    else:
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")


palavra_sorteada, dica_sorteada = pegar_palavra()

tracejado = ['_'] * len(palavra_sorteada)
letras_erradas = []
letras_certas = []
vida = 6
