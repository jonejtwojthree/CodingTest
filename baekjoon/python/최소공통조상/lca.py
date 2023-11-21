import sys
sys.setrecursionlimit(10**9)
n=int(input())

# parent[k] =a // k의 바로 위 부모는 a다
parent=[0]*(n+1)

# 각 노드의 깊이(root는 0임)
d=[0]*(n+1)

# 각 노드의 깊이가 계산됫나 확인
c=[False]*(n+1)

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int ,input().split())
    graph[a].append(b)
    graph[b].append(a)

# dfs, bfs로 바로 위 부모를 구하자
def dfs(x, depth):
    c[x]=True
    d[x]= depth

    for y in graph[x]:
        if c[y]:
            continue
        parent[y]=x
        dfs(y, depth+1)

def lca(a,b):
    # 두 노드의 깊이가 같아지게 하자
    while d[a] != d[b]:
        if d[a] > d[b]:
            b = parent[b]
        else:
            a = parent[a]
    
    while a!=b:
        a=parent[a]
        b=parent[b]
    return a

# 루트노드는 깊이가 0
dfs(1,0)
m=int(input())
for i in range(m):
    a,b = map(int, input().split())
    print(lca(a,b))
