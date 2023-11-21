def f(lst, left, right):
    if left>=right-1:
        return
    
    size=(right-left)//3
    l_idx=left+size
    r_idx=left+size*2

    lst[l_idx:r_idx]=[' ' for _ in range(r_idx-l_idx)]
    f(lst, left, l_idx)
    f(lst, r_idx, right)

while True:
    try:
        n=int(input())
        lst=['-']*(3**n)

        f(lst, 0, 3**n)
        print(''.join(lst))
    except:
        break