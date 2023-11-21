import sys

input = sys.stdin.readline

n,m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


dy=[-1,1,0,0]
dx=[0,0,-1,1]

candidate=[]
def make_color(y,x):
    global cnt
    candidate.append((y,x))
    graph[y][x]=cnt
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if 0<=ny<n and 0<=nx<m:
            if graph[ny][nx]==1:
                make_color(ny,nx)


# 섬마다 cnt를 붙여줌
cnt=2
for y in range(n):
    for x in range(m):
        if graph[y][x]==1:
            make_color(y,x)       
            cnt+=1

dd=[-1,1]
def find_short(y,x):
    my_color=graph[y][x]

    # 가로 찾기(왼쪽)
    if x-3>=0:
        for next_x in range(x-3,-1,-1):
            if graph[y][next_x] != 0  and graph[y][next_x] != my_color and graph[y][x-1] == 0 and graph[y][x-2] == 0:
                    distance = x-next_x-1
                    edges.append((distance, graph[y][x], graph[y][next_x]))
                    break
            
    # 가로 찾기(오른쪽)
    if x+3<m:
        for next_x in range(x+3,m):
            if graph[y][next_x] != 0  and  graph[y][next_x] != my_color and graph[y][x+1] == 0 and graph[y][x+2] == 0:
                    distance = next_x-x-1
                    edges.append((distance, graph[y][x], graph[y][next_x]))
                    break
            
    # 세로 찾기(위쪽)
    if y-3>=0:
        for next_y in range(y-3,-1,-1):
            if graph[next_y][x] != 0  and  graph[next_y][x] != my_color and graph[y-1][x] == 0 and graph[y-2][x] == 0:
                    distance = y-next_y-1
                    edges.append((distance, graph[y][x], graph[next_y][x]))
                    break
    
    # 세로 찾기(아래쪽)
    if y+3<n:
        for next_y in range(y+3,n):
            if graph[next_y][x] != 0 and graph[next_y][x] != my_color and graph[y+1][x] == 0 and graph[y+2][x] == 0:
                    distance = next_y-y-1
                    edges.append((distance, graph[y][x], graph[next_y][x]))
                    break
    

edges=[]
# 섬끼리 가로, 세로 최소 구하기
for y,x in candidate:
    find_short(y,x)


def kruskal():
    global cnt
    
    edges.sort()
    mnt_count=0
    parent = [i for i in range(cnt)]
    result = 0
    

    def find_parent(x):
        if x!=parent[x]:
            parent[x]=find_parent(parent[x])
        return parent[x]
    
    def union_parent(a,b):
        a=find_parent(a)
        b=find_parent(b)
        
        if a<b:
            parent[b]=a
        else:
            parent[a]=b

    for distance, a, b in edges:

        if find_parent(a) == find_parent(b):
            continue

        union_parent(a,b)
        result+=distance
        mnt_count+=1
        # print(f"{a} <-> {b} : {distance}")

    
    if mnt_count != cnt-3:
        print(-1)
    else:
        print(result)

# for ll in graph:
#     print(*ll)

# print(edges)
kruskal()