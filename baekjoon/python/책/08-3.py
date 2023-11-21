import sys
INF=sys.maxsize

x=4

arr=[0]+list(map(int,input().split()))

dp=[0]*(x+1)
dp[1]=arr[1]
dp[2]=arr[2]
dp[3]=max(arr[2], arr[1]+arr[3])

for i in range(4,x+1):
    dp[i]=max(dp[i-2]+arr[i],dp[i-1])
    # dp[i]=max(dp[i-2],dp[i-3])+arr[i]

print(dp[x])