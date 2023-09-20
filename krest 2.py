field_game = [['*', '1', '2', '3'],
         ['1', ' ', ' ', ' '],
         ['2', ' ', ' ', ' '],
         ['3', ' ', ' ', ' ']]

def field():
    print('--------------------')
    for i in range(0, 4):
        print(field_game[i])
    print('--------------------')

def winner():
    win = False
    for i in range(1, 4):
        if ((field_game[i][1] == field_game[i][2]) and
                (field_game[i][3] == field_game[i][1]) and (field_game[i][1] != ' ')):
            win = field_game[i][1]
            break
        elif ((field_game[1][i] == field_game[2][i]) and
              (field_game[3][i] == field_game[1][i]) and (field_game[1][i] != ' ')):
            win = field_game[1][i]
            break
        elif ((field_game[1][1] == field_game[2][2]) and
              (field_game[2][2] == field_game[3][3]) and (field_game[1][1] != ' ')):
            win = field_game[1][1]
            break
        elif ((field_game[1][3] == field_game[2][2]) and
              (field_game[2][2] == field_game[3][1]) and (field_game[1][3] != ' ')):
            win = field_game[1][3]
            break
        else:
            win = False
    return win

def draw():
    print('THE GAME IS OVER, friendship has won! \n THANKS FOR THE GAME!')

def deter():
    counter = 0
    for i in range(1, 4):
        counter += field_game[i].count(' ')
    if counter == 0 and winner() is False:
        dtm = 2
    elif winner():
        dtm = winner()
    else:
        dtm = counter % 2
    return dtm

def play_a():
    field()
    try:
        a, b = map(int, input(f"Player {player_a} is your turn:").split())
        (0 > a > 4) or (0 > b > 4)
    except:
        print('incorrect coordinates')
        play_a()
    else:
        if field_game[b][a] == ' ':
            field_game[b][a] = 'X'
        else:
            print('the coordinates have already been used')
    playd()

def play_b():
    field()
    if player_b == 'AI':
        pass
    else:
        try:
            a, b = map(int, input(f"Player {player_b} is your turn:").split())
            (0 > a > 4) or (0 > b > 4)
        except:
            print('incorrect coordinates')
            play_b()
        else:
            if field_game[b][a] == ' ':
                field_game[b][a] = 'O'
            else:
                print('Coordinates is used')
    playd()

def playd():
    dtm = deter()
    if dtm == 1:
        play_a()
    elif dtm == 0:
        play_b()
    elif dtm == 2:
        field()
        draw()
    else:
        if dtm == 'X':
            field()
            print(f"Player {player_a} won the game! \nCONGRATULATIONS!!!")
        elif dtm == 'O':
            field()
            print(f"Player {player_b} won the game! \nCONGRATULATIONS!!!")


print('WELKOME TO THE KRESTIKI-NOLIKI')
player_a = input('Player 1 input youre first name')
player_b = input('player 2 input youre first name')
print('\Enter the coordinates in the format:X(horizontally) Y(vertically),\nseparated by a space.')

playd()
