import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int, input().split())

dy=[1,-1,0,0]
dx=[0,0,1,-1]

graph=[]
visited = [[0 for _ in range(m)] for _ in range(n)]

for _ in range(n):
    graph.append(list(map(int, ''.join(input().split()))))

# 0,0에서 n-1, m-1까지 가야됨
def bfs():
    global n,m
    
    queue = deque([])
    # y좌표, x좌표, 벽부신 횟수
    queue.append((0,0,0))
    
    while queue:
        cur = queue.popleft()
        y,x = cur[0], cur[1]
        cnt=cur[2]

        for i in range(4):
            new_y=y+dy[i]
            new_x=x+dx[i]

            if 0<=new_y<n and 0<=new_x<m:
                if graph[new_y][new_x]==0:
                    if visited[new_y][new_x]==0:
                        visited[new_y][new_x]=visited[y][x]+1
                        queue.append((new_y, new_x, cnt))
                else:
                    if cnt==0:
                        if visited[new_y][new_x]==0:
                            visited[new_y][new_x]=visited[y][x]+1
                            queue.append((new_y, new_x, cnt+1))
    if visited[n-1][m-1]==0:
        print(-1)
    else:
        print(visited[n-1][m-1]+1)

bfs()