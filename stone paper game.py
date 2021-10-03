from random import randint
def win():
    print ('You win!')

def lose():
    print ('You lose!')

while True:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = moves[random_move]
    print('congrats you are a winner')
    if player_choice == 'paper' and computer_choice == 'scissors':
        print('computer choose scissor')
        print('sorry you lose the game computer is winner')
    elif player_choice == 'scissors' and computer_choice == 'paper':
        print('computer choose paper')
        print('congrats you are winner')
    elif player_choice == 'scissors' and computer_choice == 'rock':
        print('computer choose rock')
        print('sorry you lose the game computer is winner')
    elif player_choice == 'paper' and computer_choice == 'rock':
        print('computer choose rock')
        print(' congrats you are winner')
    elif player_choice == 'paper' and computer_choice == 'scissor':
        print('computer choose scissor')
        print('sorry you lose the game computer is winner') 
    aGain = input('Do you want to play again? (y or n)').strip()
    if aGain == 'n':
        print("you are looser!!!!")
        break