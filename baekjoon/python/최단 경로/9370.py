import sys

# 시작점에서 도착점까지의 최단거리에 교차로정점이 포함됬는지 확인하고
# 포함이 되있으면 옳은 답

from heapq import *
from collections import deque

input = sys.stdin.readline
INF = int(10**9)
T = int(input())
for _ in range(T):
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())

    graph = [[]for _ in range(n+1)]
    for _ in range(m):
        a,b,d = map(int, input().split())
        graph[a].append((b,d))
        graph[b].append((a,d))
        
    
    candidate=[]
    for _ in range(t):
        candidate.append(int(input()))

    def dijkstra(start):
        distance=[INF for _ in range(n+1)]
        distance[start]=0
        queue=[]
        heappush(queue, (start,0))

        while queue:
            tmp = heappop(queue)
            now, total_weight = tmp[0], tmp[1]

            if distance[now] < total_weight:
                continue

            for nexts in graph[now]:
                next, cost = nexts[0], nexts[1]

                if cost+total_weight < distance[next]:
                    distance[next]=cost+total_weight
                    heappush(queue, (next, cost+total_weight))
        return distance
    
    # s -> g -> h -> candi의 최단거리가 s -> candi의 최단거리와 같으면
    # 후보가 될 수 있음(둘 중 하나만 해당하면 됨)
    s_distance = dijkstra(s)
    g_distance = dijkstra(g)
    h_distance = dijkstra(h)
    
    answer=[]
    for i in candidate:
        if (s_distance[g] + g_distance[h] + h_distance[i] == s_distance[i]) or (s_distance[h] + h_distance[g] + g_distance[i]  == s_distance[i]):
            answer.append(i)
    answer.sort()
    print(*answer)
# queue = deque([(n,0)])

# N_max=100000
# distance = [sys.maxsize]*(N_max+1)
# distance[n]=0