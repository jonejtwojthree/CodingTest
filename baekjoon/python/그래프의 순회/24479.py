# # 재귀함수 쓰면 시간초과가 남
# # stack을 이용해서 풀어야됨
# import sys
# input = sys.stdin.readline

# sys.setrecursionlimit(1000000)

# n, m, r = map(int, input().split())

# graph = [[] for x in range(n+1)]
# visited = [0]*(n+1)

# for _ in range(m):
#     x, y = map(int, input().split())
#     graph[x].append(y)
#     graph[y].append(x)

# for e in graph:
#     e.sort()

# k = 1
# def dfs(r):
#     global k
#     visited[r] = k
#     k += 1
#     for i in graph[r]:
#         if visited[i] == 0:
#             dfs(i)

# dfs(r)

# for i in range(1, n+1):
#     print(visited[i])

import sys
sys.setrecursionlimit(10**9)
            
N,M,R = map(int, input().split())
visited = [False]*(N+1)
visited_cnt=[0]*(N+1)

E = [[]for i in range(N+1)]
cnt=1

for _ in range(M):
    a,b = map(int, input().split())
    
    E[a].append(b)
    E[b].append(a)

for e in E:
    e.sort() # 뺄때는 오른차순

stack=[R]

while stack:
    cur = stack.pop()
    if visited[cur]==True:
        continue

    visited[cur]=True

    visited_cnt[cur]=cnt
    cnt+=1
    
    # 재귀는 for문안에서 다른 재귀함수를 호출해서 재귀함수 호출이 끝나면 다른 간선을 찾는데
    # stack을 사용하면 그렇게 할 수 없으므로 역순으로 집어넣어 놔야됨
    for v in E[cur]:
        if visited[v]==False:
            stack.append(v)

for i in range(1,N+1):
    print(visited_cnt[i])

