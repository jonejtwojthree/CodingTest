# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
 
# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
 
# 노드의 개수 입력받기
n = int(input())
parent = [0] * (n + 1) # 부모 테이블 초기화

# 모든 간선을 담을 리스트와, 최종 비용을 담을 변수
edges = []
result = 0

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, n + 1):
    parent[i] = i

x = []
y = []
z = []

# 모든 노드?에 대한 좌표 값 입력받기
# 모든 노드인지는 모르지만 최소비용은 구할 수 있음
for i in range(1, n + 1):
    data = list(map(int, input().split()))
    x.append((data[0], i))
    y.append((data[1], i))
    z.append((data[2], i))

x.sort()
y.sort()
z.sort()

# 인접한 노드들로부터 간선 정보를 추출하여 처리
# 모든 노드인지는 모르지만 최소비용은 구할 수 있음
for i in range(n - 1):
    # 비용순으로 정렬하기 위해서 튜플의 첫 번째 원소를 비용으로 설정
    edges.append((x[i + 1][0] - x[i][0], x[i][1], x[i + 1][1]))
    edges.append((y[i + 1][0] - y[i][0], y[i][1], y[i + 1][1]))
    edges.append((z[i + 1][0] - z[i][0], z[i][1], z[i + 1][1]))

# 간선을 비용순으로 정렬
edges.sort()

# 간선을 하나씩 확인하며
for edge in edges:
    cost, a, b = edge
    # 사이클이 발생하지 않는 경우에만 집합에 포함
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)


## 메모리 초과
# import sys


# def find_parent(planet):
#     if parent_table[planet] == planet:
#         return planet
#     else:
#         parent_table[planet] = find_parent(parent_table[planet])
#         return parent_table[planet]

# def union_parent(planet1, planet2):
#     parent1 = find_parent(planet1)
#     parent2 = find_parent(planet2)

#     parent_table[parent2] = parent1


# if __name__ == "__main__":
#     result = 0

#     N = int(sys.stdin.readline())
#     planet_location_list = []

#     for i in range(N):
#         x, y, z = map(int, sys.stdin.readline().split())
#         planet_location_list.append([x, y, z])


#     edge_between_planet_list = []
#     for planet1 in range(N - 1):
#         for planet2 in range(planet1 + 1, N):
#             x = abs(planet_location_list[planet1][0] - planet_location_list[planet2][0])
#             y = abs(planet_location_list[planet1][1] - planet_location_list[planet2][1])
#             z = abs(planet_location_list[planet1][2] - planet_location_list[planet2][2])
#             edge_between_planet_list.append([planet1, planet2, min(x, y, z)])
#     edge_between_planet_list.sort(key=lambda v: v[2])

#     parent_table = [i for i in range(N)]
#     for planet1, planet2, distance in edge_between_planet_list:
#         if find_parent(planet1) != find_parent(planet2):
#             result += distance
#             union_parent(planet1, planet2)

#     print(result)