import sys
from collections import deque

n,k = map(int, sys.stdin.readline().split())
_max = sys.maxsize
visited = [_max]*(100001)

queue = deque()
queue.append(n)
visited[n]=0

d = [-1,1,2]
while queue:
    pos = queue.popleft()
    weight=visited[pos]
    
    if pos==k:
        continue
    
    for next in [pos-1, pos+1, 2*pos]:
        if 0<=next<100001:
            # if visited[next]==_max or weight+1 < visited[next]:
            if visited[next]==_max:
                visited[next]=weight+1
                queue.append(next)

print(visited[k])