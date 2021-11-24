import random


class Player:

    def __init__(self, name, isturn, guess_number):
        self.name = name
        self.is_turn = isturn
        self.guess_number = guess_number

    @classmethod
    def create_player(cls, x):
        name, isturn, guess_number = x.split('-')
        return cls(name, isturn, int(guess_number))


how_many = int(input('How many players : '))
player_List = []
for player in range(how_many):
    correct_num = input('name --> ') + '-False-0'
    e = Player.create_player(correct_num)
    player_List.append(e)

player_List[0].is_turn = True

maxi = int(input('max: '))
mini = int(input('min: '))

correct_num = random.randrange(mini, maxi + 1)

cond = True
index = 0
while cond:
    for player in player_List:
        print()
        print('Guessed ' + str(player.guess_number) + ' times already')
        if player.is_turn == True:
            print(player.name + ' making cond guess')
            guess = int(input(' --> '))
            player.guess_number += 1
            index += 1
            player_List[index % how_many].is_turn = True
            if guess == correct_num:
                print(player.name + ' found the answer')
                cond = False
                break

            elif correct_num > guess >= mini:
                print('HIGHER')

            elif correct_num < guess <= maxi:
                print('LOWER')

            else:
                print('Invalid Value')
