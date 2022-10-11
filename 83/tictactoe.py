board = {0:[' ','1','2','3'], 1:['1','-','-','-'], 2:['2','-','-','-'], 3:['3','-','-','-']}
playing_board = board

def print_board():
    for row in playing_board:
        row_concat = ""
        for column in range(4):
            row_concat += f"{playing_board[row][column]}  "
        print(row_concat)

def place_xo(player_num):
    if player_num == 1:
        character = 'X'
    elif player_num == 2:
        character = 'O'

    col_number = int(input("Please enter the column number: "))
    row_number = int(input("Please enter the row number: "))

    if col_number > 3 or col_number < 0:
        print("Column number out of range.")
        return -1
    elif row_number > 3 or row_number < 0:
        print("Row number out of range.")
        return -1
    if playing_board[row_number][col_number] == '-':
        playing_board[row_number][col_number] = character
    else:
        print("Please choose an empty slot.")
        return -1

def check_for_win(board_in):
    if board_in[2][2] != '-' and board_in[1][1] == board_in[2][2] and board_in[2][2] == board_in[3][3]:
        print(f"The winner is {board_in[2][2]}")
        return True
    elif board_in[2][2] != '-' and board_in[1][3] == board_in[2][2] and board_in[2][2] == board_in[3][1]:
        print(f"The winner is {board_in[2][2]}")
        return True
    else:
        for n in range(1,4):
            if board_in[n][2] != '-' and board_in[n][1] ==  board_in[n][2] and board_in[n][2] ==  board_in[n][3]:
                print(f"The winner is {board_in[n][1]}")
                return True
            elif board_in[2][n] != '-' and board_in[1][n] ==  board_in[2][n] and board_in[2][n] ==  board_in[3][n]:
                print(f"The winner is {board_in[1][n]}")
                return True
        if '-' not in board_in[1] and '-' not in board_in[2] and '-' not in board_in[3]:
            print("Game is a tie")
            return True
        return False

is_won = False
current_player = 1
print_board()

while is_won == False:
    return_value = place_xo(current_player)
    is_won = check_for_win(playing_board)
    print_board()
    if return_value != -1:
        if current_player == 1:
            current_player = 2
        else:
            current_player = 1