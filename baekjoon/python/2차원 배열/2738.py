import sys

n, m = map(int, sys.stdin.readline().split())
lst1 = []
lst2 = []

for _ in range(n):
    lst1.append(list(map(int, sys.stdin.readline().split())))

for _ in range(n):
    lst2.append(list(map(int, sys.stdin.readline().split())))

result = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        result[i][j] = lst1[i][j] + lst2[i][j]

for row in result:
    print(*row)
