# Dab = min(Dab, Dak+Dkb)
# 모든 지점에서 다른 지역까지 최단거리를 알 수 있음

INF = int(1e9)

n=int(input())
m=int(input())

# 2차원 배열을 생성
# graph[a][b] / /그래프에 간선 정보를 입력하고 + dp테이블로도 사용
# a->b로 가는데 최소 비용
# n*n 행렬
graph= [[INF]*(n+1) for _ in range(n+1)]

# 나자신은 비용이 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0

# 간선 입력
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b] = c

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b]==INF:
            print("INF", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()