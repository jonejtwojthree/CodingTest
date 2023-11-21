import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
LOG = 21 # (20+1) // n=1,000,000일때 log2(n) = 19.9315, +1은 더미노드 떄문에

n = int(input())

# 정점마다 깊이가 20+1만큼을 만들어줌(+1은 0층을 표현???)
# parent[a][b] = k // a번 정점의 2^b번째 부모의 노드 번호
parent= [[0]*LOG for _ in range(n+1)]

# 각 노드의 깊이(root는 0임)
d=[0]*(n+1)

# 각 노드의 깊이가 계산됫나 확인
c=[False]*(n+1)

graph = [[] for _ in range(n+1)]

for _ in range(n-1):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 루트 노드부터 시작하여 깊이를 구하는 함수
def dfs(x, depth):
    d[x]=depth
    c[x] = True

    for y in graph[x]:
        if c[y]:
            continue
        # y노드의 2^0(1)번째 부모노드(바로 위의 노드)
        parent[y][0]=x
        dfs(y,depth+1)

# 전체 부모 관계를 설정하는 함수
def set_parent():
    dfs(1,0) # 루트 노드는 1번 노드
    for i in range(1, LOG):
        for j in range(1,n+1):
            # 정점j의 2^i번째 부모노드 = [정점j의 2^(i-1)번째 부모노드]의 i-1번째 부모노드
            parent[j][i]=parent[parent[j][i-1]][i-1]

def lca(a,b):
    # b가 더 깊도록(깊이가 크도록) 설정
    if d[a] > d[b]:
        a,b = b,a

    # 깊이가 같아지도록
    # 2^20 -> 2^0
    for i in range(LOG-1, -1, -1):
        if d[b]-d[a] >= (1<<i):
            b=parent[b][i]
    
    for i in range(LOG-1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
    return parent[a][0]

set_parent()

m = int(input())

for i in range(m):
    a,b = map(int, input().split())
    print(lca(a,b))
    