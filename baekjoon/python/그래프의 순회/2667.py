# dfs stack
import sys
from collections import deque

sys.setrecursionlimit(10**9)

N = int(input())

graph = []

for _ in range(N):
    graph.append(sys.stdin.readline().rstrip())

visited = [[False for _ in range(N)]for _ in range(N)]
result=[]
city_cnt=0
#############################################

def dfs(y,x):
    global city_cnt

    if y>=N or x>=N or y<0 or x<0:
        return
    
    if visited[y][x] or graph[y][x]=='0':
        return
    
    visited[y][x]=True
    city_cnt+=1

    dfs(y,x+1)
    dfs(y,x-1)
    dfs(y+1,x)
    dfs(y-1,x)

for i in range(N):
    for j in range(N):
        if graph[i][j]=='1' and visited[i][j]==False:
            dfs(i,j)
            result.append(city_cnt)
            city_cnt=0

def bfs(y,x):
    global city_cnt
    queue = deque([(y,x)])

    while queue:
        cur = queue.popleft()
        y=cur[0]
        x=cur[1]

        if y>=N or x>=N or y<0 or x<0:
            return
        
        if visited[y][x] or graph[y][x]=='0':
            return
        
        visited[y][x]=True
        city_cnt+=1

        queue.append((y,x+1))
        queue.append((y,x-1))
        queue.append((y+1,x))
        queue.append((y-1,x))
        
for i in range(N):
    for j in range(N):
        if graph[i][j]=='1' and visited[i][j]==False:
            # dfs(i,j)
            bfs(i,j)
            result.append(city_cnt)
            city_cnt=0

result.sort()
print(len(result))
for k in result:
    print(k)