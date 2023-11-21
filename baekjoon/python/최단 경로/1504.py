# import sys

# # 다익스트라 현재까지 온 거리 중에서 최소 값을 뽑기 위해 우선순위 큐 사용
# from heapq import *

# input = sys.stdin.readline

# n,e = map(int, input().split())

# graph=[[] for _ in range(n+1)]

# for _ in range(e):
#     a,b,c = map(int, input().split())
#     graph[a].append([b,c])

# v1, v2 = map(int, input().split())

# _max=sys.maxsize


# distance=[_max for _ in range(n+1)]

# def simulatoion(start,a,b,end):
#     def dijkstra(start, dest):
#         distance=[_max for _ in range(n+1)]
#         distance[start]=0

#         queue=[]
#         heappush(queue, [0, start])
        
#         while queue:
#             # 현재까지 온 총 거리, 현재위치
#             dist, cur = heappop(queue)



#             # 이게 없어도 되긴 하지만 시간 측면에서 많이 불리        
#             if distance[cur] < dist:
#                 continue

#             for nexts in graph[cur]:
#                 next = nexts[0]
#                 weight=nexts[1]
                
#                 if dist+weight < distance[next]:
#                     distance[next]=dist+weight
#                     heappush(queue, [dist+weight, next])         
#         return distance[dest]

#     result = dijkstra(start, a) + dijkstra(v1, v2) + dijkstra(v2, end)
#     return result

# result1 = simulatoion(1,v1,v2,n)
# result2 = simulatoion(1,v2,v1,n)
# if result1 >= _max and result1 >= _max:
#     print(-1)
# else:
#     print(min(result1, result2))

import sys
from heapq import *

input = sys.stdin.readline
_max=sys.maxsize

n,e = map(int, input().split())

graph=[[] for _ in range(n+1)]
for _ in range(e):
    a,b,c = map(int, input().split())
    graph[a].append([b,c])
    #반대쪽도 해주자
    graph[b].append([a,c])

v1, v2 = map(int, input().split())


def dijkstra(start):
    queue=[]
    distance=[_max for _ in range(n+1)]
    distance[start]=0

    heappush(queue, [0, start])
    
    while queue:
        # 현재까지 온 총 거리, 현재위치
        dist, cur = heappop(queue)

        # 이게 없어도 되긴 하지만 시간 측면에서 많이 불리        
        if distance[cur] < dist:
            continue

        for nexts in graph[cur]:
            next = nexts[0]
            weight=nexts[1]
            
            if dist+weight < distance[next]:
                distance[next]=dist+weight
                heappush(queue, [dist+weight, next])         
    return distance

# 다익스트라 3번하면됨
start_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

result1 = start_distance[v1] + v1_distance[v2] + v2_distance[n]
result2 = start_distance[v2] + v2_distance[v1] + v1_distance[n] 
answer = min(result1, result2)
if answer >= _max:
    print(-1)
else:
    print(answer)