# This is an easy implementation of the game rock, paper, scissors
from random import choice

# Global variables
ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

def generateMachineChoice():
    return choice([ROCK, PAPER, SCISSORS])

def getUserChoice():
    user_choice = input('Insert option (rock, paper or scissors): ').lower()
    while user_choice not in [ROCK, PAPER, SCISSORS]:
        user_choice = input('You need to choose between rock, paper or scissors: ').lower()
    return user_choice

def main():
    print(f'Welcome to {ROCK}, {PAPER}, {SCISSORS} game!!') 
    print('Enjoy and good luck!\n')
    user_points = machine_points = 0
    win_dictionary = {ROCK: SCISSORS, PAPER: ROCK, SCISSORS: PAPER}

    while user_points < 3 and machine_points < 3: # Playing until the machine or the user have three points
        user_choice = getUserChoice()
        machine_choice = generateMachineChoice()

        print(f'Your choice: {user_choice}')
        print(f'Machine choice: {machine_choice}')
        if win_dictionary[user_choice] == machine_choice:
            print('You win!')
            user_points += 1
        elif machine_choice == user_choice:
            print('Draw')
        else:
            print('You lose')
            machine_points += 1
        print(f'Your points: {user_points}')
        print(f'Machine points: {machine_points}\n')

    if user_points == 3:
        return print('Yes!!\nYou won the battle!!')
    return print('You lost the battle..\nTry again')

if __name__ == '__main__':
    main()
