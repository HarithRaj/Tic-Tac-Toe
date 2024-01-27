import time
choice=" "
board =[
    [choice, "|", choice, "|", choice],
    ["--", "--", "--", "--"],
    [choice, "|", choice, "|", choice],
    ["--", "--", "--", "--"],
    [choice, "|", choice, "|", choice]
    ]

def join_board():
    for row in board:
        joined_board = " ".join(row)
        print(joined_board)


def check_Winner():

#Checking row
    for i in range(2):
        if (board[i*2][0]=="X" and board[i*2][2]=="X" and board[i*2][4]=="X"):
            print("Player 1 Won Congratulations on your win in Tic Tac Toe!")
            exit()
        if (board[i*2][0]=="O" and board[i*2][2]=="O" and board[i*2][4]=="O"):
            print("Player 2 Won Congratulations on your win in Tic Tac Toe!")
            exit()

#Checking Col
    for i in range(2):
        if (board[0][i*2]=="X" and board[2][i*2]=="X" and board[4][i*2]=="X"):
            print("Player 1 Won Congratulations on your win in Tic Tac Toe!")
            exit()
        if (board[0][i*2]=="O" and board[2][i*2]=="O" and board[4][i*2]=="O"):
            print("Player 2 Won Congratulations on your win in Tic Tac Toe!")
            exit()

#Checking Diagonal
        if (board[0][0] =="X"and board[2][2] =="X"and  board[4][4]=="X") or (board[4][0] =="X"and board[2][2] =="X"and  board[0][4]=="X"):
            print("Player 1 Won Congratulations on your win in Tic Tac Toe!")
            exit()
        if (board[4][0] =="O"and board[2][2] =="O"and  board[0][4]=="O") or (board[0][0] =="O"and board[2][2] =="O"and  board[4][4]=="O"):
            print("Player 2 Won Congratulations on your win in Tic Tac Toe!")
            exit()

def timer(seconds):
    while seconds>0:
        print("Loading.........Please Wait!!!!")
        time.sleep(2)
        seconds-=1
        break
    

def Game():
    print("Welcome to Tic-Tac-Toe Game!")
    # join_board()
    for i in range(9):
        if  i%2== 0:
            Player = "Player 1"
            mark = "X"
        else:
            Player = "Player 2"
            mark = "O"
        while True:
            try:
                select_row=int(input(f"{Player} Select row 0/2/4: "))
                select_col=int(input(f"{Player} Select column 0/2/4: "))

                if select_row in [0, 2, 4] and select_col in [0, 2, 4] and board[select_row][select_col] ==choice:
                    board[select_row][select_col] = mark
                    break
            except ValueError:
                    print("Wrong Input")
                    continue
        join_board()
        check_Winner()
    
    return print("Tied")


timer(5)
Game()






