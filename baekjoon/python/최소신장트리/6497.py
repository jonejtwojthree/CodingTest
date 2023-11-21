import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def kruskal(edges):
    result=0
    parents=[i for i in range(m+1)]
    edges.sort()
    
    # 부모 찾기
    def find_parent(x):
        # 내가 최상위이면 부모가 나 자체임
        if x != parents[x]:
            # x의 최상위 부모로 업데이트
            parents[x] = find_parent(parents[x])
        return parents[x]

    def union_parent(a,b):
        a = find_parent(a)
        b = find_parent(b)

        # 내맘대로 합칠때 기준 정함
        if a<b:
            parents[a]=b
        else:
            parents[b]=a

    for weight, a, b in edges:
        if find_parent(a) == find_parent(b):
            continue

        result += weight
        union_parent(a,b)
    return result

while True:
    m,n = map(int, input().split())
    edges=[]

    total=0
    for _ in range(n):
        x,y,z = map(int, input().split())
        
        # 최대값으로 정렬해야됨
        edges.append((z,x,y))
        total+=z

    # dummy
    a, b= map(int, input().split())


    # 전체액수 - 최소값임
    # expensive - cheap이 아님
    # expensive = kruskal(lambda x: -x[0])
    cheap = kruskal(edges)
    print(total-cheap)

    if a==b==0:
        break