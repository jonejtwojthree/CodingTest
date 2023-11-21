import sys

INF = sys.maxsize
input = sys.stdin.readline

n = int(input())
m = int(input())


graph=[[INF for _ in range(n+1) ] for _ in range(n+1) ]

# 나자신은 비용이 0
for a in range(1,n+1):
    for b in range(1,n+1):
        if a==b:
            graph[a][b]=0


# 그래프 갱신
# graph겸 distance 배열(혼용함)
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a][b]= min(graph[a][b], c)

for k in range(1,n+1):
    for a in range(1,n+1):
        for b in range(1,n+1):
            graph[a][b] = min(graph[a][b], graph[a][k]+graph[k][b])

for x in range(1, n+1):
    for y in range(1, n+1):
        if graph[x][y] == INF: print(0, end=' ')
        else: print(graph[x][y], end=' ')
    print()