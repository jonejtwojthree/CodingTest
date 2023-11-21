import sys
from collections import deque

input = sys.stdin.readline

n=4
m=5
graph=["00110","00011","11111","00000"]
visited = [[False for _ in range(m)] for _ in range(n)]
cnt=0

def dfs(y,x):
    if visited[y][x]==True:
        return
    visited[y][x]=True
    
    for dd in [(1,0),(-1,0),(0,1),(0,-1)]:
        next_y = y+dd[0]
        next_x = x+dd[1]
        print(f"y:{y}, x:{x}, next_y:{next_y}, next_x:{next_x}")
        if 0<=next_y<n and 0<=next_x<m:
            if graph[next_y][next_x] == '0' and visited[next_y][next_x]==False:
                dfs(next_y, next_x)

def bfs(y,x):    
    queue = deque([(y,x)])
    
    while queue:
        y,x = queue.popleft()
        
        if visited[y][x]==True:
            continue
        visited[y][x]=True
        
        for dd in [(1,0),(-1,0),(0,1),(0,-1)]:
            next_y = y+dd[0]
            next_x = x+dd[1]
            
            if 0<=next_y<n and 0<=next_x<m:
                if graph[next_y][next_x] == '0' and visited[next_y][next_x]==False:
                    queue.append((next_y, next_x))
                    



for y in range(n):
    for x in range(m):
        if graph[y][x]=='0' and visited[y][x]==False:
            # dfs(y,x)
            bfs(y,x)
            cnt+=1

print(cnt)

