import random


def main():
    if game_menu() == 1:
        game_mode_1()
    else:
        game_mode_2()
    victory_check()
    print()
    who_won()


def game_menu():
    print("Witaj w grze papier, kamień nożyce.\nWybierz tryb rozgrywki: ")
    print("1. Do jednego zwycięstwa\n2. Do trzech zwycięstw(!WiP!)")
    choice = int(input())
    if choice == 1:
        return 1
    elif choice == 2:
        return 2
    else:
        print("Podano błędną wartość.")
        game_menu()


def game_mode_1():
    human_player()
    computer_player()


def game_mode_2():
    print("!WiP!")
    main()


def human_player():
    print("1. Papier\n2. Kamień\n3. Nożyce")
    player_choice = input()
    if player_choice == 1 or 2 or 3:
        return player_choice
    else:
        print("Podano błędną wartość.")
        human_player()


def computer_player():
    computer_choice = random.randint(1, 3)
    print(computer_choice)
    return computer_choice


def victory_check():
    if human_player() == 1 and computer_player() == 1:
        return 0
    elif human_player() == 1 and computer_player() == 2:
        return 1
    elif human_player() == 1 and computer_player() == 3:
        return 2
    # Human chooses paper
    elif human_player() == 2 and computer_player() == 1:
        return 1
    elif human_player() == 2 and computer_player() == 2:
        return 0
    elif human_player() == 2 and computer_player() == 3:
        return 2
    # Human chooses rock
    elif human_player() == 3 and computer_player() == 1:
        return 2
    elif human_player() == 3 and computer_player() == 2:
        return 1
    elif human_player() == 3 and computer_player() == 3:
        return 0
    else:
        return 9
    # Human chooses scissors

    # Probably there is a better solution for victory checking perhaps assigning values to list and checking there.
    # However caused by time issues i have to leave it like that for now.


def who_won():
    if victory_check() == 2:
        print("Wygrałeś")
    elif victory_check() == 1:
        print("Przegrałeś")
    elif victory_check() == 0:
        print("Remis")
    elif victory_check() == 9:
        print("Błąd")


main()
