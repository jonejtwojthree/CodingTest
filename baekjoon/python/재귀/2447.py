def f(lst, x1, y1, x2, y2):
    if x1>=x2-1 or y1>=y2-1:
        return
    
    x_size=(x2-x1)//3
    y_size=(y2-y1)//3

    new_x1 = x1+x_size
    new_y1 = y1+y_size
    
    new_x2 = x1+x_size*2
    new_y2 = y1+y_size*2
    
    for y in range(new_y1,new_y2):
        for x in range(new_x1,new_x2):
            lst[y][x]=' '

    f(lst,x1,y1,new_x1,new_y1)
    f(lst,new_x1,y1,new_x2, new_y1)
    f(lst,new_x2,y1,x2,new_y1)

    f(lst,x1,new_y1,new_x1,new_y2)
    f(lst,new_x2,new_y1,x2,new_y2)

    f(lst,x1,new_y2,new_x1,y2)
    f(lst,new_x1,new_y2,new_x2,y2)
    f(lst,new_x2,new_y2,x2,y2)

n = int(input())

lst =[[ '*' for i in range(n)] for i in range(n)]

f(lst, 0, 0, n, n)
for ll in lst:
    print(''.join(ll))
