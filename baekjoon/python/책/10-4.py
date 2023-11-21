from collections import deque
import copy

v = int(input())
# 각 과목당 위상
indegree = [0]*(v+1)

# 누구랑 연결됬나
graph = [[] for _ in range(v+1)]

# 각과목당 시간
time = [0]*(v+1)


for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i]=data[0]
    for x in data[1:]:
        indegree[i] +=1
        graph[x].append(i)

def topology_sort():
    result = copy.deepcopy(time)
    q = deque()

    # 최초 시작
    for i in range(1,v+1):
        if indegree[i]==0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now]+time[i])
            indegree[i]-=1

            if indegree[i]==0:
                q.append(i)

    for i in range(1,v+1):
        print(result[i])

topology_sort()