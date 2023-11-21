import re
import sys
input = sys.stdin.readline

n=int(input())
arr = [[1 for _ in range(n+1)] for _ in range(n+1)]

k=int(input())
apples = [list(map(int, input().split())) for _ in range(k)]
for y,x in apples:
    arr[y][x]=-1

l=int(input())
directions = [list(map(int, input().split())) for _ in range(l)]

tail_y=0
tail_x=0
y=1
x=1

direction = 0 # 0:동, 1:남, 2:서, 3:북
dy=[1,0,0,-1]
dx=[0,1,-1,0]
cnt=0

for weight, next_direction in directions:
    
    for _ in range(weight):
        next_y = y+dy[direction]
        next_x = x+dx[direction]
        
        if 0<next_x<=n and 0<next_y<=n:
            # 나의 몸통이 있다면
            if arr[next_y][next_x] == 0:
                break
            # 사과가 있다면
            elif arr[next_y][next_x] == -1:
                arr[next_y][next_x]=0
            # 아무것도 없다면(1)
            else:
                arr[next_y][next_x]=0
                arr[tail_y][tail_x]=1

            y,x = next_y, next_x
                
        else:
            break

    
    
