# 신장트리
# 하나의 그래프가 있을 때 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

# 최소신장트리
# n개의 노드, n-1개의 간선, 최소 비용

# 크루스칼 알고리즘
# cost를 기준으로 edges정렬(그래프 사용X)
# 사이클 발생여부를 확인하며 추가
def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a=find_parent(a)
    b=find_parent(b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e = map(int, input().split())
#최초 나의 부모는 나
parent = [ i for i in range(v+1)]
edges=[]
result=0

for i in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))
edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        result+=cost
