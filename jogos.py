import forca
import adivinhacao


def escolhe_jogo():
    print("*********************************")
    print("*******Escolha o seu jogo!*******")
    print("*********************************")

    print("(1) Forca (2) Adivinhação")

    jogo = int(input("O que deseja jogar? "))

    if(jogo == 1):
        print("Jogando: Forca")
        forca.play()
    elif(jogo == 2):
        print("Jogando: Adivinhação")
        adivinhacao.play()


if(__name__ == "__main__"):
    escolhe_jogo()
