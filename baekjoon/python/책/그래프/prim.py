# 신장트리
# 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

# 최소신장트리
# n개의 노드, n-1개의 간선, 최소 비용

# 프림 알고리즘
# start 필요(다익스트라와 비슷)
# 현재 노드와 연결된 간선의 가중치가 낮은 순서대로 추출(heapq)(그래프 사용O)
# visited를 통해 방문여부 확인하며 수행(다익스트라와 같음)

from heapq import *
import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[]for _ in range(n+1)]
visited = [False]*(n+1)

for _ in range(m):
    u,v,weight = map(int, input().split())

    # 추가를 할때 weight, start, dest순으로 추가
    # start를 넣는 이유는 mst배열에 추가할때 (start, dest)처럼 넣으려고

    graph[u].append((weight, u, v))
    graph[v].append((weight, v, u))
    
# 다익스트라와 비슷하게 heapq를 사용(deque 아님)
def prim(start):
    # mst정점들 모아두는 리스트
    mst=[]
    total_weight=0

    visited[start]=True

    # 시작정점과 연결된 간선들을 모두 가져옴
    heap = graph[start]

    # 가져온 리스트를 heap으로 만듬
    heapify(heap)
    
    while heap:
        # heap에 있는 item들 중에 가중치가 제일 작은 item을 pop
        # 다익스트라 느낌
        weight, st, dest = heappop(heap)

        # 가보지 않은 정점이면
        if visited[dest] == False:
            visited[dest]=True
            total_weight += weight

            #mst에 업데이트
            mst.append((st,dest))

            for edge in graph[dest]:
                # edge[2]는 next임
                if visited[edge[2]] == False:
                    heappush((heap, edge))

    return total_weight

print(prim(1))
