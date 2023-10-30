n, m = map(int, input().split())
lst = [0 for i in range(n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for idx in range(i,j+1):
        lst[idx]=k
print(*lst[1:])
