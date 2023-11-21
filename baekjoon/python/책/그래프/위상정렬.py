# 위상정렬
# 순서가 정해져(단방향 그래프)있는 일련의 작업을 차례대로 수행해야 할 떄 사용(선입선출 deque)
# weight는 없지만 위상이 존재

from collections import deque

v,e=map(int, input().split())
indegree=[0]*(v+1)
graph=[[] for i in range(v+1)]

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

def topology_sort():
    result=[]
    q=deque()

    # 최초 시작할때 위상이 0인 노드들 추가(start 없으니까)
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)
    
    while q:
        now = q.popleft()
        result.append(now)

        for i in graph[now]:
            indegree[i]-=1
            if indegree[i]==0:
                q.append(i)

    for i in result:
        print(i, end=' ')
topology_sort()