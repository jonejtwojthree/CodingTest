import sys
import math
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n=int(input())
LOG = int(math.log2(n))+1
graph=[[] for _ in range(n+1)]
parent = [[0]*LOG for i in range(n+1)]
visited = [False]*(n+1)
d = [0]*(n+1)

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(x, depth):
    visited[x]=True
    d[x]=depth

    for y in graph[x]:
        if visited[y]:
            continue
        parent[y][0]=x
        dfs(y,depth+1)

def lca(a,b):
    # b가 더 깊게 하려고
    if d[a] > d[b]:
        a,b = b,a
    
    # a와 b의 깊이가 동일해지게
    # break하면 안됨
    for i in range(LOG-1, -1,-1):
        if d[b]-d[a] >= (1<<i):
            b = parent[b][i]
    
    if a==b:
        return a
    
    for i in range(LOG-1,-1,-1):
        if parent[a][i] != parent[b][i]:
            a=parent[a][i]
            b=parent[b][i]

    return parent[a][i]

# 각 노드의 바로 윗 부모 갱신하기
dfs(1,0)

# 2^i번째 부모 찾기
for i in range(1,LOG):
    for j in range(1,n+1):
        parent[j][i] = parent[parent[j][i-1]][i-1]

m=int(input())

for _ in range(m):
    a,b = map(int, input().split())
    print(lca(a,b))



## 시간 초과
# import sys

# input = sys.stdin.readline

# n=int(input())

# graph=[[] for _ in range(n+1)]

# for _ in range(n-1):
#     a,b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)
# # print(parent)

# parent = [0 for i in range(n+1)]
# visited = [False]*(n+1)

# def dfs(cur):
#     visited[cur]=True
        
#     for next in graph[cur]:
#         if visited[next] == False:
#             parent[next]=cur
#             dfs(next)
# dfs(1)
# print(parent)

# m= int(input()) 
# for _ in range(m):
#     v1,v2 = map(int, input().split())
    
#     # index bound 위해
#     v1_parent, v2_parent = [0,v1],[0,v2]

#     while parent[v1]:
#         v1_parent.append(parent[v1])
#         v1=parent[v1]
#     while parent[v2]:
#         v2_parent.append(parent[v2])
#         v2=parent[v2]
        
#     v1_idx=len(v1_parent)-1
#     v2_idx=len(v2_parent)-1
    
#     while v1_parent[v1_idx] == v2_parent[v2_idx]:
#         v1_idx-=1
#         v2_idx-=1
#     print(v1_parent[v1_idx+1])
