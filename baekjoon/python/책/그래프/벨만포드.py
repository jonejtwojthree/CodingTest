# 다익스트라의 일반 버전(음수도 되는 다익스트라)

INF = int(1e9)

n=int(input())
m=int(input())

# 출발지에서 모든지역까지의 최단거리 기록
dist = [INF]*(n+1)

# graph 대신 edge를 받음
edges = []
for _ in range(m):
    u, v, w = map(int, input().split()) # 노드, 인접 노드, 가중치
    edges.append((u, v, w))

# 다익스트라처럼 start를 입력받음
def bf(start):
    dist[start]=0

    # n은 사이클 확인 용도
    for i in range(n):
        # edges에 있는 노드들을 n-1번 수행하고 n번째는 사이클있나 확인
        for j in range(m):
            node = edges[j][0]
            next_node = edges[j][1]
            cost = edges[j][2]

            if dist[node] != INF and dist[node]+cost < dist[next_node]:
                dist[next_node] =dist[node]+cost

                # n-1번 동안 수행되고 n번째 수행될때도 갱신이 일어나면 사이클이 발생한 것임
                if i==n:
                    return True
    return False


# 벨만 포드 알고리즘 수행
# 만약 1번 도시에서 출발해 어떤 도시로 가는 과정에서
# 시간을 무한히 오래 전으로 되돌릴 수 있다면 첫째 줄에 -1을 출력한다
# -> 음수 사이클로 -무한으로 distance가 나온다는 얘기
negative_cycle = bf(1)

if negative_cycle:
    print('-1')
else:
    # 1번 노드를 제외한 다른 모든 노드로 가기 위한 최단 거리 출력
    for i in range(2, n+1):
        if dist[i] == INF: # 도달할 수 없는 경우 -1 출력
            print('-1')
        else: # 도달할 수 있는 겨우 거리를 출력
            print(dist[i])