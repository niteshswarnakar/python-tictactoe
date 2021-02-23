board = ['-','-','-',
        '-','-','-',
        '-','-','-'
        ]

game_still_running = True
winner = None 
current_player = 'X'

def display():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def flip_player():
    global current_player
    if current_player == 'X':
        current_player = 'Y'
    else:
        current_player = 'X'

def handle_turn():
    global current_player
    count = 0
    while(count<9 and game_still_running):
        print(current_player + " turn ")
        position = input("position : ")
        position = int(position) - 1
        while(position>9):
            print("Invalid : ")
            position = input("Re enter postion : ")
            position = int(position) -1

        board[position] = current_player
        flip_player()
        display()
        count +=1
        check_if_over()

#row winner
def row_win():
    global winner
    if board[0] == board[1] == board[2]!='-':
        winner = board[0]
        return board[0]
    if board[3] == board[4] == board[5]!='-':
        
        winner = board[3]
        return board[3]
    if board[6] == board[7] == board[8]!='-':
        
        winner = board[6]
        return board[0]
#column winner
def column_win():
    global winner
    if board[0] == board[3] == board[6]!='-':
        winner = board[0]
        return board[0]
    if board[1] == board[4] == board[7]!='-':
        
        winner = board[3]
        return board[3]
    if board[2] == board[5] == board[8]!='-':
        
        winner = board[6]
        return board[0]
#diagonal winner
def diagonal_win():
    global winner
    if board[0] == board[4] == board[8]!='-':
        winner = board[0]
        return board[0]
    if board[2] == board[4] == board[6]!='-':
        winner = board[3]
        return board[3]

def check_for_winner():
    row_winner = row_win()
    col_winner = column_win()
    diag_winner = diagonal_win()
    #if row_winner or col_winner or diag_winner:
    if row_winner:
        return row_winner
    elif col_winner:
        return col_winner
    elif diag_winner:
        return diag_winner
    

def check_for_tie():
    return
def check_if_over():
    global game_still_running
    #check for winner
    if check_for_winner():
        game_still_running = False
    #check for tie
    check_for_tie()

display()
handle_turn()

if not game_still_running:
    print(winner + " won")