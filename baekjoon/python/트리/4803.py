import sys
from collections import deque

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def bfs(i):
    flag=True
    queue = deque([i])

    while queue:
        cur = queue.popleft()

        # 돌고돌아 사이클        
        if visited[cur]==True:
            return False

        visited[cur]=True

        for next in graph[cur]:
            # 혼자 사이클
            if cur == next:
                 return False
            
            if visited[next]==False:
                queue.append(next)
    return True

# start 노드부터 시작하여 DFS를 끝까지 돌고
# 사이클 존재 여부를 리턴하는 함수
parent = []
def findCycle(start):
    for adj_node in graph[start]:
        # 인접 노드가 자신의 부모 노드인 경우 패스
        if parent[start] == adj_node:
            continue
        
        # 인접 노드가 부모 노드가 아닌데 방문 이력이
        # 있다는 것은 곧 사이클을 의미함
        if visited[adj_node]:
            return True
        
        parent[adj_node] = start
        visited[adj_node] = 1
        # 인접 노드를 루트 노드로 하는 서브트리에
        # 사이클이 존재하면 곧 전체 트리에 사이클이
        # 존재하는 것과 같음
        if findCycle(adj_node):
            return True
    
    return False

case_cnt=1
while True:
    n,m = map(int, input().split())

    if n==m==0:
        break

    graph = [[] for _ in range(n+1)]
    for _ in range(m):
        a,b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    
    visited = [False]*(n+1)
    
    ret=0
    for i in range(1,n+1):
        if bfs(i):
            ret+=1

    if ret > 2:
        print(f"Case {case_cnt}: A forest of {ret} trees.")
    elif ret==1:
        print(f"Case {case_cnt}: There is one tree.")
    else:
        print(f"Case {case_cnt}: No trees.")
    case_cnt+=1