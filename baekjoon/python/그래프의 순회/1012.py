# # dfs
# import sys

# sys.setrecursionlimit(10**9)
# T = int(input())
# dy=[1,-1,0,0]
# dx=[0,0,1,-1]

# def dfs(y,x):
#     global N,M
#     if (0<=y<N and 0<=x<M) == False:
#         return
    
#     if visited[y][x]==True or graph[y][x]==0:
#         return
#     visited[y][x]=True

#     for i in range(4):
#         new_y = y+dy[i]
#         new_x = x+dx[i]
#         dfs(new_y, new_x)

# for _ in range(T):
#     M,N,K = map(int, sys.stdin.readline().split())
#     graph=[ [0 for _ in range(M)] for _ in range(N)]
#     visited=[ [False for _ in range(M)] for _ in range(N)]
    
#     for _ in range(K):
#         x,y = map(int, sys.stdin.readline().split())
#         graph[y][x]=1

#     cnt=0
#     for y in range(N):
#         for x in range(M):
#             if graph[y][x]==1 and visited[y][x]==False:
#                 cnt+=1
#                 dfs(y,x)
#     print(cnt)


# bfs
import sys
from collections import deque

sys.setrecursionlimit(10**9)

T = int(input())
dy=[1,-1,0,0]
dx=[0,0,1,-1]

def bfs(y,x):
    global N,M

    queue=deque()
    queue.append((y,x))

    while queue:
        cur=queue.popleft()
        y,x=cur[0],cur[1]

        if (0<=y<N and 0<=x<M) == False:
            return

        if visited[y][x]==True or graph[y][x]==0:
            return
        visited[y][x]=True

        for i in range(4):
            new_y = y+dy[i]
            new_x = x+dx[i]
            bfs(new_y, new_x)

for _ in range(T):
    M,N,K = map(int, sys.stdin.readline().split())
    graph=[ [0 for _ in range(M)] for _ in range(N)]
    visited=[ [False for _ in range(M)] for _ in range(N)]
    
    for _ in range(K):
        x,y = map(int, sys.stdin.readline().split())
        graph[y][x]=1

    cnt=0
    for y in range(N):
        for x in range(M):
            if graph[y][x]==1 and visited[y][x]==False:
                cnt+=1
                bfs(y,x)
    print(cnt)

