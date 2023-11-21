import sys
from collections import deque

input = sys.stdin.readline

n=5
m=6
strings=["101010","111111", "000001","111111","111111"]
graph=[[]]
for ll in strings:
    graph.append(list(map(int,ll)))

def bfs(y,x):    
    queue = deque([(y,x)])
    
    while queue:
        y,x = queue.popleft()
        for dd in [(1,0),(-1,0),(0,1),(0,-1)]:
            next_y = y+dd[0]
            next_x = x+dd[1]
            
            if 0<next_y<=n and 0<next_x<=m:
                if graph[next_y][next_x] == 1:
                    graph[next_y][next_x] = graph[y][x]+1
                    queue.append((next_y, next_x))
                    
bfs(1,1)
print(graph[n-1][m-1])
           
           
