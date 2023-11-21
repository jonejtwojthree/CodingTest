#  DFS
import sys
from collections import deque

n,m = map(int, sys.stdin.readline().split())

graph=[list(map(int, ''.join(sys.stdin.readline().split()))) for _ in range(n)]

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(y,x):
    
    for i in range(4):
        new_y = y+dy[i]
        new_x = x+dx[i]
        
        if 0 <= new_y < n and 0<= new_x < m:
            if graph[new_y][new_x] == 1 or graph[y][x]+1 < graph[new_y][new_x]:
                graph[new_y][new_x] = graph[y][x]+1
                dfs(new_y, new_x)
dfs(0,0)
print(graph[n-1][m-1])

##  BFS
# import sys
# from collections import deque
# n,m = map(int, sys.stdin.readline().split())

# graph=[list(map(int, ''.join(sys.stdin.readline().split()))) for _ in range(n)]

# dx=[0,0,1,-1]
# dy=[1,-1,0,0]

# def bfs(y,x):
#     queue = deque([(y,x)])
#     cnt=1

#     while queue:
#         cur = queue.popleft()
#         y=cur[0]
#         x=cur[1]

#         for i in range(4):
#             n_y = y+dy[i]
#             n_x = x+dx[i]        

#             if 0 <= n_y < n and 0<= n_x < m:
#                 if graph[n_y][n_x] == 1:
#                     queue.append((n_y, n_x))
#                     graph[n_y][n_x] = graph[y][x]+1
        
# bfs(0,0)
# print(graph[n-1][m-1])
