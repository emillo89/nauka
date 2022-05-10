l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
player1 = 'X'
player2 = 'O'
filled = []

print(f"""Player 1 symbol: 'X'
Player 2 sybol: 'O'""")


def show():
    '''Show the boardgame'''
    game = f' {l[0]} | {l[1]} | {l[2]} \n' \
           f'-----------\n' \
           f' {l[3]} | {l[4]} | {l[5]} \n' \
           f'-----------\n' \
           f' {l[6]} | {l[7]} | {l[8]} \n'
    print(game)


def play_game(player):
    '''Choice your number and fill in the blank
    return True if player win'''
    player_choice = int(input(f'{player} what is your number?')) - 1
    if player_choice not in filled:
        filled.append(player_choice)
        l[player_choice] = player
        if search_win(player):
            print(f'You win!')
            return True
        elif len(filled) == 9:
            print('Drawn')
        else:
            return False


def search_win():
    if l[0] == l[1] == [2] or l[3] == l[4] == l[5] or\
        l[6] == l[7] == l[8] or l[0] == l[3] == l[6] or \
        l[1] == l[4] == l[7] or l[2] == l[5] == l[8] or \
        l[0] == l[4] == l[8] or l[2] == l[4] == l[6]:
        return True

game_is_on = True
for number in range(9):
    show()
    try:
        play1 = play_game(player1)
        show()
        if play1 == True or len(filled) == 9:
            break
        else:
            play2 = play_game(player2)
            show()
            if play2 == True:
                break
    except ValueError:
        print("You have not typed anything")
    except IndexError:
        print("Number must be between 1 and 9")