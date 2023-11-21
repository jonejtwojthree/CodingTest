import sys
n=int(input())

_max = sys.maxsize
dp=[max]*(n+1)

if n==1 or n==2:
    print(n-1)
    sys.exit(0)

dp[1]=0
dp[2]=1
dp[3]=1

for i in range(4,n+1):
    if i%3==0 and i%2==0:
        dp[i]=min(dp[i//3], dp[i//2],dp[i-1])+1
    elif i%3==0:
        dp[i]=min(dp[i//3], dp[i-1])+1
    elif i%2==0:
        dp[i]=min(dp[i//2],dp[i-1])+1
    else:
        dp[i]=dp[i-1]+1

print(dp[-1])