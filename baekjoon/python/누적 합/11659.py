import sys
n,m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

# dp[k]: sum(lst[1] ~ lst[k])
# dummy 인덱스 사용

dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = dp[i-1]+lst[i-1]

for _ in range(m):
    i,j = map(int, sys.stdin.readline().split())
    print(dp[j]-dp[i-1])