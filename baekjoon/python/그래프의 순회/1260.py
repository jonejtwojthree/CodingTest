# dfs stack
import sys
from collections import deque

sys.setrecursionlimit(10**9)

N,M,R = map(int, sys.stdin.readline().split())

graph = [[]for i in range(N+1)]

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    
    graph[a].append(b)
    graph[b].append(a)
#############################################

for e in graph:
    e.sort(reverse=True) # 뺄때는 오른차순

stack=[R]
visited_dfs=[False]*(N+1)
sequence_dfs=[]

while stack:
    cur = stack.pop()
    if visited_dfs[cur]==True:
        continue
    
    visited_dfs[cur]=True
    sequence_dfs.append(cur)
    
    for v in graph[cur]:
        if visited_dfs[v] == False:
            stack.append(v)

############################################

for e in graph:
    e.sort() # 뺄때는 오른차순

queue=deque([R])
visited_bfs=[False]*(N+1)
sequence_bfs=[]

while queue:
    cur = queue.popleft()
    if visited_bfs[cur]==True:
        continue

    visited_bfs[cur]=True
    sequence_bfs.append(cur)
    
    for v in graph[cur]:
        if visited_bfs[v]==False:
            queue.append(v)

print(*sequence_dfs, sep=' ')
print(*sequence_bfs, sep=' ')

