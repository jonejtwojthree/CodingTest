# bfs든 dfs든 2번을 돌아야됨
# 최초에 내가 1번을 선택해서 돌았으면 1번에서 먼거지 전체에서 먼것인지는 알 수 없음
# 최초에 먼저 돌고 마지막 인덱스값을 리턴받고 그것을 start로 해서 다시 돌리고 나오면 최종값

import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

v= int(input())

graph = [[] for _ in range(v+1)]

# visited[k] =a k까지 오는데 a걸림

for _ in range(v):
    tmp = list(map(int, input().split()))
    
    start=tmp[0]
    tmp_idx=1
    while tmp[tmp_idx]!=-1:
        end = tmp[tmp_idx]
        weight = tmp[tmp_idx+1]

        graph[start].append((end, weight))
        
        tmp_idx+=2


# def bfs(i):
#     queue = deque([i])
#     visited = [-1]*(v+1)
#     visited[i]=0

#     res=[0,0]
#     while queue:
#         cur = queue.popleft()

#         for nexts in graph[cur]:
#             next=nexts[0]
#             weight=nexts[1]     
            
#             if visited[next]==-1:
#                 queue.append(next)
#                 visited[next] = visited[cur]+weight

#                 if res[1] < visited[next]:
#                     res[0]=next
#                     res[1]=visited[next]
#     return res
# # 1에서 임의로 시작 했지만 과연 1에서 시작하는게 맞나?
# # 그래서 bfs를 1번돈 후 1번 더 돌면 됨 
# result, _ = bfs(1)
# print(bfs(result)[1])

def dfs(cur):
    global res
    for nexts in graph[cur]:
            next=nexts[0]
            weight=nexts[1]

            if visited[next]==-1:
                visited[next]=visited[cur]+weight
                if visited[res] < visited[next]:
                    res=next   
                dfs(next)


visited = [-1]*(v+1)
res=1
visited[res]=0
dfs(res)

visited = [-1]*(v+1)
visited[res]=0
dfs(res)

print(max(visited))

    