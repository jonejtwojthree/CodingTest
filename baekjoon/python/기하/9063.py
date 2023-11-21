N = int(input())

lx = []
ly = []
for _ in range(N):
    a, b = map(int, input().split())
    lx.append(a)
    ly.append(b)
    print((max(lx) - min(lx)) * (max(ly) - min(ly)))
