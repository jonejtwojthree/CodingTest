from collections import deque
import sys


N, M, R = map(int, sys.stdin.readline().rstrip().split())
visited=[0]*(N+1)
E = [[] for _ in range(N+1)]

for _ in range(M):
    a,b = map(int, sys.stdin.readline().split())
    E[a].append(b)
    E[b].append(a)

for lst in E:
    lst.sort(reverse=True)

cnt=1

queue=deque([])
queue.append(R)

while queue:
    cur = queue.popleft()
    if visited[cur]!= 0:
        continue
    
    visited[cur]=cnt
    cnt+=1

    for v in E[cur]:
        if visited[v]== 0:
            queue.append(v)

print(*visited[1:], sep='\n')

