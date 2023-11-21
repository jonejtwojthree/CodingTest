import sys
from heapq import *

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v,e = map(int, input().split())
edges=[]
graph = [[]for _ in range(v+1)]

for _ in range(e):
    a,b,c = map(int, input().split())
    # weight, start, dest
    edges.append((c,a,b))
    graph[a].append((c, a, b))
    graph[b].append((c, b, a))


def kruskal():
    edges.sort()    
    total_weight=0

    # 최초 자기자신이 최고 조상임
    parent=[i for i in range(v+1)]

    def find_parnet(x):
        if x != parent[x]:
            parent[x]=find_parnet(parent[x])
        return parent[x]
    
    def union_parent(a,b):
        a=find_parnet(a)
        b=find_parnet(b)

        if a<b:
            parent[a]=b
        else:
            parent[b]=a
    
    for cost, a, b in edges:
        parent_a = find_parnet(a)
        parent_b = find_parnet(b)
        
        # cycle 발생
        if parent_a == parent_b:
            continue
        else:
            union_parent(a,b)
            total_weight+=cost
    return(total_weight)

def prim(start):
    mst=[]
    total_weight = 0

    visited=[False]*(v+1)
    visited[start]=True
    
    heap = graph[start]
    
    heapify(heap)

    while heap:
        weight, st, dest = heappop(heap)

        if visited[dest]==True:
            continue

        visited[dest]=True
        total_weight+=weight

        for edge in graph[dest]:
            if visited[edge[2]] == False:
                heappush(heap, edge)
    return total_weight

# print(kruskal())
print(prim(1))

