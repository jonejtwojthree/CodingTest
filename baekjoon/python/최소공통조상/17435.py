import sys
import math
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

m=int(input())
LOG = int(math.log2(m))+1
f = [0]+list(map(int,input().split()))
dp = [[f[i]] for i in range(m+1)]

for j in range(1, LOG):
    for i in range(1,m+1):
        dp[i].append(dp[dp[i][j-1]][j-1])
        
q = int(input())
for _ in range(q):
    n,x = map(int, input().split())
    for i in range(LOG-1,-1,-1):
        if n >= 1<<i:
            x=dp[x][i]
            n -= 1<<i
    print(x)
    
    # for i in range(LOG-1, -1,-1):
    #   if d[b]-d[a] >= (1<<i):
    #         b = parent[b][i]

    
## 시간 초과
# import sys

# input = sys.stdin.readline

# m = int(input())
# parent = [0]+list(map(int, input().split()))

# q = int(input())
# for _ in range(q):
#     n, x = map(int, input().split())
#     for _ in range(n):
#         x = parent[x]
#     print(x)