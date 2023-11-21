def f(row, col, size):
    # global result

    # print('===================================')
    # print(f"row: {row}, col: {col}, size: {size}")
    # print(f"white: {white}, blue: {blue}")
    # print('===================================')

    color = lst[row][col]
    result=''
    for i in range(size):
        for j in range(size):
            if lst[row+i][col+j] != color:
                result+="("

                new_size=size//2
                result += f(row, col, new_size)
                result += f(row,col+new_size, new_size)
                result += f(row+new_size, col, new_size)
                result += f(row+new_size, col+new_size, new_size)
                
                result+=")"
                return result
    
    if lst[row][col]=='1':
        result+='1'
    else:
        result+='0'            
    return result
          

import math

n = int(input())

lst = [input() for _ in range(n)]
result=""

if n==1:
    if lst[0][0]=='1':
        print('(1)')
    else:
        print('0')
else:
    print(f(0,0,n))
