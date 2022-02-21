import random


# TicTacToe by Wallis

# Prints board
def print_board(board):
    print('\n' * 20)
    print('{:^9} | {:^9} | {:^9}'.format(board[1], board[2], board[3]))
    print('-' * 32)
    print('{:^9} | {:^9} | {:^9}'.format(board[4], board[5], board[6]))
    print('-' * 32)
    print('{:^9} | {:^9} | {:^9}'.format(board[7], board[8], board[9]))


# player 1 chooses if he/she wants to be X or O
def player_xo():
    while True:
        x = input('Does player 1 wants to be X or O? ')
        if x == 'X' or x == 'O':
            return x
        else:
            print('Wrong input, try again')
            continue


# Function to place a marker
def place_marker(board, marker, position):
    board[position] = marker


# Function that checks if someone won
def win_check(board, mark):
    if board[1] == mark and board[2] == mark and board[3] == mark:
        return True
    elif board[4] == mark and board[5] == mark and board[6] == mark:
        return True
    elif board[7] == mark and board[8] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[3] == mark and board[6] == mark and board[9] == mark:
        return True
    elif board[1] == mark and board[5] == mark and board[9] == mark:
        return True
    elif board[3] == mark and board[5] == mark and board[7] == mark:
        return True


# Function that returns 1 or 2 for determining who goes first
def turn_one():
    return random.randint(0, 1)


# Function that checks if position on board is available
def available_board(board, position):
    if board[position] == '':
        return True
    else:
        return False


# Function that checks if board is not full
def full_board(board):
    if '' in board:
        return True
    else:
        return False


# Taking position from player
def player_choice(board):
    while True:
        x = int(input('Choose a position to place your marker(1-9): '))
        if x in [1, 2, 3, 4, 5, 6, 7, 8, 9] and available_board(board, x):
            return x
        else:
            print('Wrong input, please try again')
            continue


# Replay function
def replay():
    x = input('Do you wish to play again(Y/N)? ')
    if x == 'Y':
        return True
    else:
        return False


while True:
    game_board = ['#', '', '', '', '', '', '', '', '', '']
    print('Welcome to the Tic Tac Toe game made in Python by Wallis.')
    input('Press Enter to continue... ')

    turn = turn_one()
    x_o = player_xo()
    if x_o == 'X' and turn == 0:
        players = ['X', 'O']
    elif x_o == 'X' and turn == 1:
        players = ['O', 'X']
    elif x_o == 'O' and turn == 0:
        players = ['O', 'X']
    else:
        players = ['X', 'O']

    while True:
        # First player
        print_board(game_board)
        print("{}'s turn".format(players[0]))
        ppos_1 = player_choice(game_board)
        place_marker(game_board, players[0], ppos_1)
        if win_check(game_board, players[0]):
            print('\n' * 2)
            print('{} Won!'.format(players[0]))
            break
        if not full_board(game_board):
            print('\n' * 2)
            print('Draw!')
            break

        # Second player
        print_board(game_board)
        print("{}'s turn".format(players[1]))
        ppos_2 = player_choice(game_board)
        place_marker(game_board, players[1], ppos_2)
        if win_check(game_board, players[1]):
            print('\n' * 2)
            print('{} Won!'.format(players[1]))
            break
        if not full_board(game_board):
            print('\n' * 2)
            print('Draw!')
            break

    rpl = replay()

    if rpl:
        continue
    else:
        break
