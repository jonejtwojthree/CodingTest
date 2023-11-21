import sys
INF=sys.maxsize

x=26
dp=[0]*(x+1)

dp[2]=1
dp[3]=1
dp[4]=2
dp[5]=1

for i in range(6,x+1):
    result=INF

    if i%5==0:
        result = min(result,dp[i//5]+1)
    
    if i%3==0:
        result = min(result,dp[i//3]+1)
    
    if i%2==0:
        result = min(result,dp[i//2]+1)
    
    result = min(result, dp[i-1]+1)
    dp[i]=result

print(dp[x])
