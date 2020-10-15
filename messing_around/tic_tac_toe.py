# TacTacToe

import numpy as np

#Define Playing Field and vars
field = np.array([["~", "~", "~"],
                 ["~", "~", "~"],
                 ["~", "~", "~"]])


def print_field(field):
    print(" 1 2 3  --> X-Cords")
    for i in range(0, 3):
        print(i + 1, field[i][0] + field[i][1] + field[i][2])



def is_game_over(field):

    #Check Horizontal for both players
    for i in range(0, 3):
        if field[i][0] == 'X' and field[i][1] == 'X' and field[i][2] == 'X':
            return True
        if field[i][0] == 'O' and field[i][1] == 'O' and field[i][2] == 'O':
            return True

    #Check Vertical
    for i in range(0, 3):
        if field[0][i] == 'X' and field[1][i] == 'X' and field[2][i] == 'X':
            return True
        if field[0][i] == 'O' and field[1][i] == 'O' and field[2][i] == 'O':
            return True

    #Check Diagonal

    if field[0][0] == 'X' and field[1][1] == 'X' and field[2][2] == 'X':
        return True
    if field[0][0] == 'O' and field[1][1] == 'O' and field[2][2] == 'O':
        return True
    if field[2][0] == 'X' and field[1][1] == 'X' and field[0][2] == 'X':
        return True
    if field[2][0] == 'O' and field[1][1] == 'O' and field[0][2] == 'O':
            return True


def set_board(x, y, field, player):
    if player == 'X':
        field[y - 1][x - 1] = 'X'
        return field
    if player == 'O':
        field[y - 1][x - 1] = 'O'
        return field


print_field(field)

#main Loop
while True:
    #Player 1 Move
    x = int(input("Player 1 type in your x"))
    y = int(input("Player 1 type in your y"))

    set_board(x, y, field, 'X')
    print_field(field)
    if is_game_over(field):
        print("Player 1 Won!!!")
        break

    #Player 2 Move
    x = int(input("Player 2 type in your x"))
    y = int(input("Player 2 type in your y"))

    set_board(x, y, field, 'O')
    print_field(field)
    if is_game_over(field):
        print("Player 2 Won!!!")
        break
