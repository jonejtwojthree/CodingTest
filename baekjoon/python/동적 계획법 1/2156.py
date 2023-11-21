import sys
n=int(input())

wine=[0]
dp=[0]*(n+1)

for _ in range(n):
    wine.append(int(input()))

if n==1 or n==2:
    print(sum(wine))
    sys.exit(0)

dp[1]=wine[1]
dp[2]=wine[1]+wine[2]
dp[3]=max(wine[1]+wine[2], wine[1]+wine[3], wine[2]+wine[3])

if n==3:
    print(dp[3])

for i in range(4,n+1):
    dp[i]=max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i-1]+wine[i])

print(dp)