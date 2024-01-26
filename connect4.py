"""
The plan
maker a basic connect 4 game
what do we need
board
pieces
user interaction
"""
import random
def take_turn(p):
    print("Player ",p)
    print("Enter a spot Number between 1 and 7")
    n = int(input())
    bottom = 5
    while board[bottom] [n] != " ":
        bottom = bottom -1
    if p==1:
        board[bottom] [n]
        board[bottom] [n] = "x"
    
    if p==2:
        board[bottom] [n]
        board[bottom] [n] = "y"
        
    print_board()
def computer_turn():
    print("Computer Turn")
    n = random.randint(1,7)
    
    bottom = 5
    while board[bottom] [n] != " ":
        bottom = bottom -1
    
       
    board[bottom] [n] = "o"
    
    
    print_board()
    
def print_board():
    for row in board:
        print(*row)
    print()
    
board = [
        ["|"," "," "," "," "," ","|"],
        ["|"," "," "," "," "," ","|"],
        ["|"," "," "," "," "," ","|"],
        ["|"," "," "," "," "," ","|"],
        ["|"," "," "," "," "," ","|"],
        ["|"," "," "," "," "," ","|"]
        ]



while True:
    take_turn(1)
    print_board()
    computer_turn()
    
    

    
