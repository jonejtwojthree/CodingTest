import sys
from heapq import *

sys.setrecursionlimit(10**9)
input = sys.stdin.readline


n,m = map(int, input().split())

lst=[]
for _ in range(n):
    x,y = map(int, input().split())
    lst.append((x,y))

edges=[]
graph=[[] for _ in range(n+1)]

for i in range(n):
    x1=lst[i][0]
    y1=lst[i][1]

    for j in range(i+1,n):
        x2=lst[j][0]
        y2=lst[j][1]

        distance = round(((x2-x1)**2+(y2-y1)**2)**0.5,2)
        edges.append((distance, i+1,j+1))
        graph[i+1].append((distance,i+1,j+1))
        graph[j+1].append((distance,j+1,i+1))

ways=[]
for _ in range(m):
    a,b = map(int, input().split())
    ways.append((a,b))

def kruskal():
    edges.sort()

    parent = [i for i in range(n+1)]
    result = 0


    def find_parent(x):
        if x!=parent[x]:
            parent[x]=find_parent(parent[x])
        return parent[x]
    
    def union_parent(a,b):
        a=find_parent(a)
        b=find_parent(b)
        
        if a<b:
            parent[b]=a
        else:
            parent[a]=b

    for way_a,way_b in ways:
        for distance, cur_a,cur_b in edges:
            if way_a==cur_a and way_b == cur_b:
                # 이미 연결되어 있어서 distance 할 필요 없음
                # result+=distance
                union_parent(cur_a, cur_b)
                break

    edges.sort()
    for distance, a, b in edges:

        if find_parent(a) == find_parent(b):
            continue

        union_parent(a,b)
        result+=distance
    return result

def prim():

    visited = [False]*(n+1)
    result=0

    heap=[]
    
    # ways에 있는 간선들을 true해줘야됨
    for a,b in ways:
        visited[a]=True
        visited[b]=True

        heap+=graph[a]
        heap+=graph[b]

    heapify(heap)

    while heap:
        distance, start, dest = heappop(heap)

        if visited[dest]==True:
            continue

        visited[dest]=True
        result+=distance

        for edge in graph[dest]:
            if visited[edge[2]]==False:
                heappush(heap, edge)
    return result

# result=prim()
result=kruskal()
print(f"{result:.2f}")
