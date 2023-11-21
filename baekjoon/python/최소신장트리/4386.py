import sys
from heapq import * # prim

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n=int(input())


lst=[]
for _ in range(n):
    x,y=map(float, input().split())
    lst.append((x,y))

edges = [] # kruskal
graph = [[] for _ in range(n+1)] # prim

for i in range(n):
    x1 = lst[i][0]
    y1 = lst[i][1]
    for j in range(i+1,n):
        x2 = lst[j][0]
        y2 = lst[j][1]
        weight = round(((x2-x1)**2 + (y2-y1)**2)**0.5,2)
        
        # kruskal
        edges.append((weight, i, j))
        
        # prim
        graph[i].append((weight, i,j))
        graph[j].append((weight, j,i))
        


# kruskal(greedy)
# 간선을 가중치순으로 정렬하고
# 각 간선의 최상위 부모노드를 확인하는 배열을 만듬(사이클 확인용도)
def kruskal():
    edges.sort()
    parent = [i for i in range(n+1)]

    def find_parent(x):
        if x != parent[x]:
            parent[x]=find_parent(parent[x])
        return parent[x]

    def union_parnet(a,b):
        a = find_parent(a)
        b = find_parent(b)

        if a<b:
            parent[b]=a
        else:
            parent[a]=b


    result=0
    for weight,a,b in edges:
        # 사이클 발생
        if find_parent(a) == find_parent(b):
            continue
        
        union_parnet(a,b)
        result += weight
    return result

def prim(start):
    mst = []
    visited = [False]*(n+1)
    result = 0

    heap = graph[start]
    visited[start]=True
    
    heapify(heap)

    while heap:
        weight, start, dest = heappop(heap) 

        if visited[dest]==False:
            visited[dest]=True
            result += weight

            mst.append((start, dest))

            for edge in graph[dest]:
                if visited[edge[2]]==False:
                    heappush(heap, edge)
    return result

# result = kruskal()
result = prim(1)
print(result)
