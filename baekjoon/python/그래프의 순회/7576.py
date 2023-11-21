import sys
from collections import deque

input = sys.stdin.readline

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def my_bfs():
    m,n = map(int, input().split())
    graph=[]
    queue = deque([])

    for i in range(n):
        tmp = list(map(int, input().split()))
        for j in range(len(tmp)):
            if tmp[j]==1:
                # 익은 토마토 좌표 모두를 큐에 저장해놔야 함
                queue.append((i,j))
        graph.append(tmp)

    while queue:
        cur=queue.popleft()
        y=cur[0]
        x=cur[1]

        for i in range(4):
            new_y=y+dy[i]
            new_x=x+dx[i]

            if 0<=new_y<n and 0<=new_x<m and graph[new_y][new_x]==0:
                graph[new_y][new_x]=graph[y][x]+1
                queue.append((new_y, new_x))
    
    _max = 0
    for lst in graph:
        if 0 in lst:
            print(-1)
            return
        else:
            _max=max(_max, max(lst))
    print(_max-1)
my_bfs()
    