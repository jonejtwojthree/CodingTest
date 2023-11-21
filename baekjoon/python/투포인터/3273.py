import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int, input().split()))
x=int(input())

lst.sort() # 정렬하고 투포인터 사용

left=0
right=len(lst)-1

cnt=0
while left<right:
    print(left, right, lst[left]+lst[right])
    _sum = lst[left]+lst[right]
    if _sum==x:
        cnt+=1
        left+=1
    elif _sum <x:
        left+=1
    else:
        right-=1    

print(cnt)