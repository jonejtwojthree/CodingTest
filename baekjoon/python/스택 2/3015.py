import sys

n=int(input())
stack=[]
result=0
for _ in range(n):
    num = int(input())
    cnt=0
    while stack:
        if stack[-1] < num:
            stack.pop()
            cnt+=1
    if cnt==1:
        result+=1
    elif cnt>1:
        result += (cnt*(cnt-1)//2)
        result+=cnt
    stack.append(num)

print(result)