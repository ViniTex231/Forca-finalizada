import nutella
import cafecomleite
import raiz


def menu():
    while True:
        print("==BEM VINDO AO JOGO DA FORCA!==")
        print("Modos de jogo: ")
        print("[1] - Nutella")
        print("[2] - Café com Leite")
        print("[3] - Raiz")
        jogo = input("Digite o jogo que deseja jogar: ")
        print('')
        if jogo == "1":
            nutella.visual()
            nutella.apresentacao()
            nutella.funcionamento(nutella.vida)
        elif jogo == "2":
            cafecomleite.visual()
        elif jogo == "3":
            raiz.visual()
        else:
            print("Opção incorreta, digite uma das opções. ")

menu()
