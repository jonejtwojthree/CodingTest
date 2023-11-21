import sys
N, S = map(int, input().split())
array = [int(x) for x in sys.stdin.readline().rstrip().split()]
# 문제조건에 의해서 정렬 안하고 해야함

left=0
right=0
result=array[0]
length=sys.maxsize

while left<=right:
    if result >=S:
        length=min(length, right-left+1)
        result-=array[left]
        left+=1
    else:
        right+=1
        if right<N:
            result+=array[right]
        else:
            break

if length==sys.maxsize:
    print(0)
else:
    print(length)