def f(row, col, size):
    global minus_one, zero, one
    # print('===================================')
    # print(f"row: {row}, col: {col}, size: {size}")
    # print(f"white: {white}, blue: {blue}")
    # print('===================================')

    
    color = lst[row][col]
    for i in range(size):
        for j in range(size):
            if lst[row+i][col+j] != color:
                new_size=size//3
                f(row, col, new_size)
                f(row,col+new_size, new_size)
                f(row,col+new_size*2, new_size)
                
                f(row+new_size, col, new_size)
                f(row+new_size,col+new_size, new_size)
                f(row+new_size,col+new_size*2, new_size)
                
                f(row+new_size*2, col, new_size)
                f(row+new_size*2,col+new_size, new_size)
                f(row+new_size*2,col+new_size*2, new_size)
                return
            
    if color==1:
        one+=1
    elif color==0:
        zero+=1
    else:
        minus_one+=1

n = int(input())

lst = [list(map(int, input().split())) for _ in range(n)]
minus_one = zero = one = 0

f(0, 0, n)

print(minus_one)
print(zero)
print(one)