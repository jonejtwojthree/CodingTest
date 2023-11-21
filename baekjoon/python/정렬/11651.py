n = int(input())

lst = []
for _ in range(n):
    a,b = map(int,input().split())
    lst.append([a,b])

lst.sort(key=lambda x: (x[1], x[0]))
for l in lst:
    print(*l)