import sys
input=sys.stdin.readline

n,m=map(int, input().split())
lst=[]

for _ in range(n):
    a,b=map(int, input().split())

    #  역순만 필요함
    if a>b:
        # b부터 저장
        # 구간 구하려고
        lst.append((b,a))

lst.sort()
distance=0
start = lst[0][0]
end = lst[0][1]

for i in range(1,len(lst)):
    next_start=lst[i][0]
    next_end=lst[i][1]
    
    if next_start > end:
        distance += (end-start)*2
        start=next_start
        end=next_end
    else:
        # 1-5
        # 3-4 로 그을 수 있음
        end = max(end, next_end)
distance += (end-start)*2
distance += m
print(distance)