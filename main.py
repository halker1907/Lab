import tkinter as tk
import random
import os
CANVAS_BG = 'red'
COLS = 25
ROWS = 15

WALL = '▓'
EMPTY = '░'
maze = []

"""
1.список списка или список строк
2.Полностью заполнить лабиринт стенами
3.Количество колонн и рядов - нечетное
4.бульд начинает сносить стены в четных клетках
5.если в двух клетках от него стены - ломает обе
6.когда во всех четных клетках нет стен лабиринт проходим
7.надо по границам обрисовать стеной, и сделать вход с выходом
"""
for row_idx in range(ROWS):
    row = []
    for col in range(COLS):
        row.append(WALL)
    maze.append(row)

buldozer_col = random.choice(range(0, COLS, 2))
buldozer_row = random.choice(range(0, ROWS, 2))
maze[buldozer_row][buldozer_col] = '@'

for i in range(100):
    buldozer_direction = []
    if buldozer_col + 2 < COLS:
        buldozer_direction.append('right')
    if buldozer_col - 2 >= 0:
        buldozer_direction.append('left')
    if buldozer_row + 2 < ROWS:
        buldozer_direction.append('down')
    if buldozer_row - 2 >= 0:
        buldozer_direction.append('up')

    if not buldozer_direction:
        print('опа')
        break

    direction = random.choice(buldozer_direction)
    if direction == 'right':
        if maze[buldozer_row][buldozer_col + 2] == WALL:
            maze[buldozer_row][buldozer_col + 1] = EMPTY
            maze[buldozer_row][buldozer_col + 2] = EMPTY
        buldozer_col += 2
    elif direction == 'left':
        if maze[buldozer_row][buldozer_col - 2] == WALL:
            maze[buldozer_row][buldozer_col - 1] = EMPTY
            maze[buldozer_row][buldozer_col - 2] = EMPTY
        buldozer_col -= 2
    elif direction == 'up':
        if maze[buldozer_row - 2][buldozer_col] == WALL:
            maze[buldozer_row - 1][buldozer_col] = EMPTY
            maze[buldozer_row - 2][buldozer_col] = EMPTY
        buldozer_row -= 2
    elif direction == 'down':
        if maze[buldozer_row + 2][buldozer_col] == WALL:
            maze[buldozer_row + 1][buldozer_col] = EMPTY
            maze[buldozer_row + 2][buldozer_col] = EMPTY
        buldozer_row += 2

    os.system('cls')
    for row in maze:
        print(*row, sep='')
