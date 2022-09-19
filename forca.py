import random


def play():

    opening()

    secret_word = load_secret_word()

    correct_letters = load_correct_letters(secret_word)

    hang = False
    correct = False
    errors = 0

    print(correct_letters)

    while(not correct and not hang):
        kick = request_kick()

        if(kick in secret_word):
            marca_chute_correto(kick, correct_letters, secret_word)
        else:
            errors += 1
            draw_gallows(errors)

        hang = errors == 6
        correct = "_" not in correct_letters
        print(correct_letters)

    if(correct):
        winner_message()
    else:
        loser_message(secret_word)


def opening():
    print("*********************************")
    print("***Bem-vindo ao Jogo da Forca!***")
    print("*********************************")


def load_secret_word():
    file = open("words.txt", "r")
    words = []

    for line in file:
        line = line.strip()
        words.append(line)

    file.close()

    number = random.randrange(0, len(words))
    secret_word = words[number].upper()
    return secret_word


def load_correct_letters(word):
    return ["_" for letter in word]


def request_kick():
    kick = input("Escolha uma letra.\n")
    kick = kick.strip().upper()  # remove os caracteres indesejados e passa para maiúsculo
    return kick


def marca_chute_correto(kick, correct_letters, secret_word):
    index = 0
    for letter in secret_word:
        if(kick == letter):
            # print("Encontrei a letter {} na posição {}".format(letter, index))
            correct_letters[index] = letter
        index += 1


def draw_gallows(errors):
    print("  _______     ")
    print(" |/      |    ")

    if(errors == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(errors == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(errors == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(errors == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(errors == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(errors == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (errors == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def winner_message():
    print("\nParabéns, você venceu!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


def loser_message(secret_word):
    print("\nQue pena, você foi enforcado!")
    print("A palavra era {}.".format(secret_word))
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


if(__name__ == "__main__"):
    play()
