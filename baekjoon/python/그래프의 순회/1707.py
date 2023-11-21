# 이분 그래프
# 나와 연결된 정점은 나와 다른색으로 칠해져 있어야 함

import sys
from collections import deque

def bfs(size, start):
    queue = deque([])

    colors[start]=0
    queue.append(start) # 1번째부터 시작, 0번째색상
    
    while queue:
        cur = queue.popleft()

        for v in graph[cur]:
            new_color=(colors[cur]+1)%2
            if colors[v]== -1:
                colors[v]= new_color
                queue.append(v) # 1번째부터 시작, 0번째색상                
            else:# 칠해야할 색상이 이미 들어가 있으면
                if colors[v] == new_color:
                    continue
                else:
                    return False
    return True

input = sys.stdin.readline
k = int(input())
for _ in range(k):
    v,e = map(int, input().split())
    
    graph = [[] for _ in range(v+1)]

    for _ in range(e):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    colors =[-1]*(v+1)
    # 모든 정점에서 한번씩 시작해봐서 모두 통과되면 yes
    for i in range(1,v+1):
        if colors[i] == -1: # 시간초과 방지를 위해 갔나 안갔나 확인
            result = bfs(v, i)
            if not result:
                break
    print("YES" if result else "NO")
