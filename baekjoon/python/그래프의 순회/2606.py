# # dfs stack
# import sys
# sys.setrecursionlimit(10**9)

# N = int(input())
# M = int(input())
# R=1

# visited = [False]*(N+1)
# graph = [[]for i in range(N+1)]

# for _ in range(M):
#     a,b = map(int, sys.stdin.readline().split())
    
#     graph[a].append(b)
#     graph[b].append(a)

# for e in graph:
#     e.sort(reverse=True) # 뺄때는 오른차순

# stack=[R]

# while stack:
#     cur = stack.pop()
#     if visited[cur]==True:
#         continue

#     visited[cur]=True    
    
#     for v in graph[cur]:
#         if visited[v]==False:
#             stack.append(v)

# print(sum(filter(lambda x: x==True, visited))-1)

#dfs recursion
import sys
sys.setrecursionlimit(10**9)

N = int(input())
M = int(input())
R=1

visited = [False]*(N+1)
graph = [[]for i in range(N+1)]

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    
    graph[a].append(b)
    graph[b].append(a)

for e in graph:
    e.sort(reverse=True) # 뺄때는 오른차순

stack=[R]

def dfs(R):
    if visited[R]==True:
        return
    visited[R]=True    
    
    for v in graph[R]:
        if visited[v]==False:
            dfs(v)
            
dfs(R)
print(sum(filter(lambda x: x==True, visited))-1)