import sys
from heapq import *

def topology_lst():
    queue=[]
    result = []
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        queue.sort()
        cur = queue.pop(0)
        result.append(cur)
        
        for next in graph[cur]:
            indegree[next] -=1
            if indegree[next]==0:
                queue.append(next)
    print(*result)

def topology_heapq():
    queue=[]
    result = []
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)

    heapify(queue)

    while queue:
        cur = heappop(queue)
        result.append(cur)
        
        for next in graph[cur]:
            indegree[next] -=1
            if indegree[next]==0:
                heappush(queue, next)
    print(*result)


input = sys.stdin.readline

n,m = map(int ,input().split())

indegree=[0 for _ in range(n+1)]
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b=map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

# 앞문제부터 푸는게 좋으니깐 heapq를 써야함
topology_heapq()

