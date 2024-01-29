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
    join_board()
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
    
    print("Match Tied")

def func():
    print("OBJECTIVE")
    print() 
    print("The game is played by two players, typically X and O, who take turns marking spaces in a 3x3 grid. The goal is to be the first to get three of your symbols (X or O) in a row, either horizontally, vertically, or diagonally.")
    print()
    input('PRESS ENTER KEY TO VIEW INSTRUCTIONS')
    print()
    print("INSTRUCTIONS")
    print()
    print("1.The top-left cell is at coordinates (0, 0).\n2.The top-center cell is at coordinates (0, 2).")
    print("3.The top-right cell is at coordinates (0, 4).\n4.The middle-left cell is at coordinates (2, 0).")
    print("5.The middle-center cell is at coordinates (2, 2).\n6.The middle-right cell is at coordinates (2, 4).")
    print("7.The bottom-left cell is at coordinates (4, 0).\n8.The bottom-center cell is at coordinates (4, 2).")
    print("9.The bottom-right cell is at coordinates (4, 4).")
    print()
    print("How to Decide the Winner")
    print()
    print("1. Winning Conditions: The game ends when one player achieves three of their symbols in a row, either horizontally, vertically, or diagonally.\n   The player who achieves this first is declared the winner..")
    print("2. Draw Condition: If all cells are filled and no player has achieved three in a row, the game is a draw.")
    print()
    input('PRESS ENTER KEY TO START THE GAME')

timer(5)
print()
func()
print()
Game()
