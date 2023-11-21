import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())

# indegree배열은 차수를 저장함
# 출발지, 목적지를 입력받을때 목적지 인덱스의 차수를 증가시킴
indegree = [0]*(n+1)
graph = [[]for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    indegree[b]+=1

def topologt_sort():
    result = []
    queue = deque()

    # 차수가 없는 정점을 큐에 삽입
    for i in range(1,n+1):
        if indegree[i]==0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        
        # 결과출력 위해
        result.append(current)

        for i in graph[current]:
            indegree[i]-=1
            if indegree[i]==0:
                queue.append(i)

    for i in result:
        print(i)

topologt_sort()