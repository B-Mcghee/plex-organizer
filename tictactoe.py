theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def print_board(board):
    print(f'{board["top-L"]}|{board["top-M"]}|{board["top-R"]}')
    print('-+-+-')
    print(f'{board["mid-L"]}|{board["mid-M"]}|{board["mid-R"]}')
    print('-+-+-')
    print(f'{board["low-L"]}|{board["low-M"]}|{board["low-R"]}')


theBoard2 = {'top-L': 'O', 'top-M': ' ', 'top-R': 'O',
             'mid-L': 'X', 'mid-M': 'X', 'mid-R': 'X',
             'low-L': 'O', 'low-M': ' ', 'low-R': 'O'}


turn = 'X'
for i in range(9):
    print_board(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

print_board(theBoard)
