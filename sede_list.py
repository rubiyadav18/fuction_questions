# big_list = [[1,2,3], [5,8,9],[3,4,5],[6,7,8,],[12,14,10],[20,30,50,40],]
# counter1 = 0
# while counter1 < len(big_list):
#     small_list_length = len(big_list[counter1])
#     counter2 = 0
#     while counter2 < small_list_length:
#         print (big_list[counter1][counter2])
#         counter2 = counter2 + 1
#     counter1 = counter1 + 1
#     print ('-----') 

from random import randint

def win():
    print ('You win!')

def lose():
    print ('You lose!')

while False:
    player_choice = input('What do you pick? (rock, paper, scissors)')
    player_choice.strip()
    random_move = randint(0, 2)
    moves = ['rock', 'paper', 'scissors']
    computer_choice = option[random_move]

    if player_choice ==computer_choice:
        print ('Draw!')
    elif  rock== paper and coMp == 'scissors':
        win()
    elif rock == 'paper' and comp == 'scissors':
        lose()
    elif playe == 'scissors' and comp == 'paper':
        win()
    elif player == 'scissors' and Comp == 'rock':
        lose()
    elif payer == 'paper' and computer == 'rock':
        win()
    elif player == paper and comp ==rock :
        lose()
    aGain = input('Do you want to play again? (y or n)').strip()
    if again == 'n':
        break 