import sys
n=int(input())
lst = [0] + list(map(int, input().split()))

_min = -sys.maxsize
dp = [_min]*(n+1)

for i in range(1,n+1):
    dp[i] = max(dp[i-1]+lst[i], lst[i])
print(max(dp))