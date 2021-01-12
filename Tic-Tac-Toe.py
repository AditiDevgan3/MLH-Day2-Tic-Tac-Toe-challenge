# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 22:05:32 2021

@author: Aditi Devgan
"""

def display_board(board): 
    print(" "+"|"+" "+"|")
    print(board[7]+"|"+board[8]+"|"+board[9])
    print(" "+"|"+" "+"|")
    print("------")
    print(" "+"|"+" "+"|")
    print(board[4]+"|"+board[5]+"|"+board[6])
    print(" "+"|"+" "+"|")
    print("------")
    print(" "+"|"+" "+"|")
    print(board[1]+"|"+board[2]+"|"+board[3])
    print(" "+"|"+" "+"|")
    


def initiate_board():
    board = ["#"," ", " ", " ", " ", " ", " ", " ", " ", " "]
    return board


myBoard = initiate_board()
display_board(myBoard)
        
def place_marker(board, marker, position): 
    board[position] = marker
    

def win_check(board, mark):   
    return horizontal_check(board) or vertical_check(board) or diagonal_check(board)

def horizontal_check(board):
    si = 7
    for i in range(3):
        if board[si] == board[si+1] == board[si+2] != " ":
            return True
        si -= 3
    return False

def vertical_check(board):
    si = 1
    for i in range(3):
        if board[si] == board[si+3] == board[si+6] != " ":
            return True
        si+=1
    return False

def diagonal_check(board):
    if board[1] == board[5] == board[9] != " ":
        return True
    elif board[3] == board[5] == board[7] != " ":
        return True
    else:
        return False

def choose_first():
    print("What player will move first?")
    print("Type 1 for player X \nType 2 for player O")
    first = int(input())
    if first == 1:
        return "X"
    elif first == 2:
        return "O"
    pass

def space_check(board, position):  
    if board[position] == " ":
        return True
    else:
        return False

def full_board_check(board):    
    if " " in board:
        return False
    else:
        return True


def replay():    
    print("Do you want to play again?[Y/N]")
    r = input()
    if r.lower() == "y":
        main()
    else:
        print("GoodBye!")
        

def play(mark,board):
    while not win_check(board,mark) and not full_board_check(board):
        placeHolder = int(input())
        if space_check(board, placeHolder):
            place_marker(board, mark, placeHolder)
        else:
            print("Invaild Position")
            continue
        display_board(board)
        if mark == "X":
            mark = "O"
        else:
            mark = "X"
    if win_check(board, mark):
        if mark == "X":
            print("Winner is O")
        else:
            print("Winner is X")
    if full_board_check(board):
        print("Draw")
    replay()

        
def main(): 
    print('Welcome to Tic Tac Toe!')
    mark = choose_first()
    board = initiate_board()
    play(mark,board)
    

main()