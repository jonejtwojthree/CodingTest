def f(row, col, size):
    global white, blue
    # print('===================================')
    # print(f"row: {row}, col: {col}, size: {size}")
    # print(f"white: {white}, blue: {blue}")
    # print('===================================')
    if size==1:
        if lst[row][col]==1:
            blue+=1
        else:
            white+=1
        return
    
    color = lst[row][col]
    for i in range(size):
        for j in range(size):
            if lst[row+i][col+j] != color:
                new_size=size//2
                f(row, col, new_size)
                f(row,col+new_size, new_size)
                f(row+new_size, col, new_size)
                f(row+new_size, col+new_size, new_size)
                return

    if lst[row][col]==1:
        blue+=1
    else:
        white+=1

import math

n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]

white=0
blue=0

f(0, 0, n)
print(white)
print(blue)