n,m=map(int, input().split())
coins = [ int(input()) for _ in range(n)]
INF = int(1e9)
dp=[INF]*(m+1)



# for coin in coins:
#     for i in range(1,m+1):
#         if i%coin==0:
#             dp[i] = min(dp[i], i//coin)

dp[0]=0
for coin in coins:
    for i in range(1,m+1):
        if dp[i-coin]!=INF:
            dp[i] = min(dp[i], dp[i-coin]+1)


print(-1 if dp[m]==INF else dp[m])

