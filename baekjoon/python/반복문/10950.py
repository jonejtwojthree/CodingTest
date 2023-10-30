n = int(input())
lst = [ list(map(int, input().split())) for _ in range(n)]
for i,j in lst:
    print(i+j)