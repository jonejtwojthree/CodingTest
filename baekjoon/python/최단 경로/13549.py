
import sys

# 다익스트라 현재까지 온 거리 중에서 최소 값을 뽑기 위해 우선순위 큐 사용
from heapq import *
from collections import deque

input = sys.stdin.readline

n,k = map(int, input().split())

queue = deque([(n,0)])

N_max=100000
distance = [sys.maxsize]*(N_max+1)
distance[n]=0

while queue:
    nows = queue.popleft()
    now=nows[0]
    weight=nows[1]

    if now==k:
        print(weight)
        break
    
    next = now*2
    if 0<=next<=N_max and weight< distance[next]:
        queue.append((now*2, weight))
        distance[next]=weight+1

    next = now-1
    if 0<=next<=N_max and weight+1 < distance[next]:
        queue.append((now-1, weight+1))
        distance[next]=weight+1
        
    next = now+1
    if 0<=next<=N_max and weight+1 < distance[next]:
        queue.append((now+1, weight+1))
        distance[next]=weight+1


# INT = int(1e9)

# v,e = map(int, input().split())
# start = int(input())

# graph=[[] for _ in range(v+1)]

# for _ in range(e):
#     u,e,w = map(int, input().split())
#     graph[u].append([e,w])

# # _max=sys.maxsize 
# _max = INT

# distance=[_max for _ in range(v+1)]

# # print(graph)

# def dijkstra(start):
#     distance[start]=0

#     queue=[]
#     heappush(queue, [0, start])
    
#     while queue:
#         # 현재까지 온 총 거리, 현재위치
#         dist, cur = heappop(queue)


#         # 이게 없어도 되긴 하지만 시간 측면에서 많이 불리        
#         if distance[cur] < dist:
#             continue

#         for nexts in graph[cur]:
#             next = nexts[0]
#             weight=nexts[1]
            
#             if dist+weight < distance[next]:
#                 distance[next]=dist+weight
#                 heappush(queue, [dist+weight, next])
                
# dijkstra(start)
# for item in distance[1:]:
#     print("INF" if item == _max else item)
