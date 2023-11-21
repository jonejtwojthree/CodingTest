import sys

input = sys.stdin.readline
n = int(input())

lst = []
for _ in range(n):
    x,y = map(int, input().split())
    lst.append((x,y))

lst.sort()
distance=0
start = lst[0][0]
end = lst[0][1]

for i in range(1,n):
    next_start=lst[i][0]
    next_end=lst[i][1]
    
    if next_start > end:
        distance += (end-start)
        start=next_start
        end=next_end
    else:
        # 1-5
        # 3-4 로 그을 수 있음
        end = max(end, next_end)
distance += (end-start)
print(distance)