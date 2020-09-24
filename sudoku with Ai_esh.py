import numpy as np
import pyautogui as pg
import time

board = []

while True:
    row = list(input('Row: '))
    ints = []

    for n in row:
        ints.append(int(n))
    board.append(ints)

    if len(board) == 9:
        break
    print('Row ' + str(len(board)) + ' Complete')

time.sleep(3)


def check(x,y,n):
#check row
    for row in range(0,9):
        if board[row][x] == n and row != y:
            return False
#check col
    for col in range(0,9):
        if board[y][col] == n and col != x:
            return False
#check box
    x0 = (x // 3) * 3 # take the box and re-adj in the corner box
    y0 = (y // 3) * 3
    for X in range(x0, x0 + 3):
        for Y in range(y0, y0 + 3):  # Checks for numbers in box(no matter the position, it finds the corner)
            if board[Y][X] == n:
                return False
    return True

def Print(matrix):
    final = []
    str_fin = []
    for i in range(9):
        final.append(matrix[i])

    for lists in final:
        for num in lists:
            str_fin.append(str(num))

    counter = []

    for num in str_fin:
        pg.press(num)
        pg.hotkey('right')
        counter.append(num)
        if len(counter) % 9 == 0:
            pg.hotkey('down')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')
            pg.hotkey('left')


def solve ():
    global board
    for y in range(9):
        for x in range(9):
            if board[y][x] == 0:
                for n in range(1,10):
                    if check(x,y,n):
                        board[y][x] = n
                        solve()
                        board[y][x] = 0  #if the number is not fit make the space zero again
                return
    Print(board)
    input("again ?")

solve()