def f(start, end):
    if start>end:
        return None
    
    mid = (start+end)//2
    
    if array[mid]==mid:
        return mid
    elif array[mid] >mid:
        return f(start, mid-1)
    else:
        return f(mid+1, start)
    
n=int(input())
array=list(map(int, input().split()))

index = f(0,n-1)

if index==None:
    print(-1)
else:
    print(index)