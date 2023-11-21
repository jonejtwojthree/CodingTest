import sys

INF = sys.maxsize

input = sys.stdin.readline
v,e =map(int, input().split())

# 부모 테이블 초기화(사이클 여부 판단하기 위해)
# parent[x]=a x의 최상위 부모는 a이다
parents = [0]*(v+1)

edges=[]
total_cost=0

for _ in range(e):
    a,b, cost = map(int, input().split())
    # 간선을 추가할때 cost가 먼저오게 함(정렬을 위해)
    edges.append((cost,a,b))

# cost순으로 정렬
edges.sort()

# 부모 찾기
def find_parent(x):
    # 내가 최상위이면 부모가 나 자체임
    if x != parents[x]:
        # x의 최상위 부모로 업데이트
        parents[x] = find_parent(parents[x])
    return parents[x]

def union_parent(a,b):
    a = find_parent[a]
    b = find_parent[b]

    # 내맘대로 합칠때 기준 정함
    if a<b:
        parents[a]=b
    else:
        parents[b]=a

# kruskal 알고리즘 수행
for i in range(e):
    cost, a, b = edges[i]

    # cycle발생해서 continue
    if find_parent(a) == find_parent(b):
        continue
    else: # cycle이 아니면 서로 다른 부모를 1개로 합침
        union_parent(a,b)
        total_cost+=cost
print(total_cost)