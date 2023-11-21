import sys
from collections import deque

input = sys.stdin.readline

dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
def my_bfs():
    m,n,h = map(int, input().split())
    graph=[]
    queue = deque([])

    for i in range(h):
        graph.append([])
        for j in range(n):
            tmp = list(map(int, input().split()))
            for k in range(len(tmp)):
                if tmp[k]==1:
                # 익은 토마토 좌표 모두를 큐에 저장해놔야 함
                    queue.append((i,j,k)) # z,y,x
            graph[i].append(tmp)

    while queue:
        cur=queue.popleft()
        z=cur[0]
        y=cur[1]
        x=cur[2]

        for i in range(6):
            new_z=z+dz[i]
            new_y=y+dy[i]
            new_x=x+dx[i]

            if 0<=new_z<h and 0<=new_y<n and 0<=new_x<m and graph[new_z][new_y][new_x]==0:
                graph[new_z][new_y][new_x]=graph[z][y][x]+1
                queue.append((new_z,new_y, new_x))
    
    _max = 0
    for lst in graph:
        for l in lst:
            if 0 in l:
                print(-1)
                return
            else:
                _max=max(_max, max(l))
    print(_max-1)
my_bfs()
    