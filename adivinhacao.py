import random


def play():
    print("*********************************")
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("*********************************")

    secret_number = random.randrange(1, 101)
    total_attempts = 0
    points = 1000

    print("\nQual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    level = int(input("\nNível de dificuldade escolhido: "))

    if(level == 1):
        total_attempts = 20
    elif(level == 2):
        total_attempts = 10
    else:
        total_attempts = 5

    for round in range(1, total_attempts + 1):
        print("\nTentativa {} de {}".format(round, total_attempts))

        kick_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", kick_str)
        kick = int(kick_str)

        if(kick < 1 or kick > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        correct = kick == secret_number
        bigger = kick > secret_number
        smaller = kick < secret_number

        if(correct):
            print("Você acertou e obteve {} pontos!".format(points))
            break
        else:
            lost_points = abs(secret_number - kick)
            points = points - lost_points
            if(bigger):
                print("O seu chute foi maior do que o número secreto.")
                if (round == total_attempts):
                    print("\nVocê errou! O número secreto era {}.\nVocê obteve {} pontos.".format(
                        secret_number, points))
            elif(smaller):
                print("O seu chute foi menor do que o número secreto.")
                if (round == total_attempts):
                    print("\nVocê errou! O número secreto era {}.\nVocê obteve {} pontos.".format(
                        secret_number, points))

    print("\nFim de jogo.")


if(__name__ == "__main__"):
    play()
