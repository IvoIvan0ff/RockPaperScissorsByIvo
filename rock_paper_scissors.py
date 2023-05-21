import colorama
from colorama import Fore
import random

rock = 'Rock'
paper = 'Paper'
scissors = 'Scissors'
computer_score = 0
player_score = 0

while True:
    player_move = input(Fore.BLUE + "Choose [r]ock, [p]aper or [s]cissors: ")

    if player_move == 'r':
        player_move = rock
    elif player_move == 'p':
        player_move = paper
    elif player_move == 's':
        player_move = scissors
    else:
        print(Fore.BLUE + "Invalid Input. Try Again...")
        player_second_input = input(Fore.BLUE + "Please type [yes] to PLay Again or [no] to quit: ")
        if player_second_input.lower() == 'no':
            print(Fore.WHITE + "Exiting.... See you again!:)")
            break
        elif player_second_input.lower() == 'yes':
            continue
        else:
            print(Fore.WHITE + "Invalid Input. Exiting ...")
            print(Fore.WHITE + "See you again!:)")
            break

    computer_random_number = random.randint(1, 3)
    computer_move = ""

    if computer_random_number == 1:
        computer_move = rock
    elif computer_random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(Fore.BLUE + f"The computer chose {computer_move}.")

    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        player_score += 1
        print(Fore.GREEN + "You win!")
        print(Fore.BLUE + f'Score: {player_score} : {computer_score}')
    elif player_move == computer_move:
        print(Fore.YELLOW + "Draw!")
        print(Fore.BLUE + f'Score: {player_score} : {computer_score}')
    else:
        computer_score += 1
        print(Fore.RED + "You lose!")
        print(Fore.BLUE + f'Score: {player_score} : {computer_score}')

    player_second_input = input(Fore.BLUE + "Please type [yes] to PLay Again or [no] to quit: ")

    if player_second_input.lower() == 'no':
        print(Fore.WHITE + "Exiting.... See you again!:)")
        break
    elif player_second_input.lower() == 'yes':
        continue
    else:
        print(Fore.WHITE + "Invalid Input. Exiting ...")
        print(Fore.WHITE + "See you again!:)")
        break


