import sys
from heapq import *

input = sys.stdin.readline
INF = int(1e9)

n,m = map(int, input().split())
start=int(input())
graph=[[]for i in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]

    heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now = heappop(q)
        if distance[now] < dist:
            continue
        
        for nexts in graph[now]:
            next=nexts[0]
            cost = dist + nexts[1]
            
            if cost < distance[next]:
                distance[next] = cost
                heappush(q, (cost, next))

dijkstra(start)

for i in range(1,n+1):
    if distance[i]==INF:
        print("INF")
    else:
        print(distance[i])