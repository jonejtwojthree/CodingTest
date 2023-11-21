import sys
import math

def isSosu(x):
    if x==0 or x==1:
        return False
    if x==2:
        return True
    
    for i in range(2, int(math.sqrt(x))+1): # 범위를 줄여줌
        if x % i == 0:
            return False
    return True


lst = []

_max = 0
while True:
    n = int(input())
    if n==0:
        break
    if n>_max:
        _max=n
    lst.append(n)

dp=[0]*(_max*2+1)
dp[2]=1

for i in range(3,_max*2+1):
    if isSosu(i):
        dp[i] = dp[i-1]+1
    else:
        dp[i]=dp[i-1]

for i in lst:
    print(dp[2*i]-dp[i])
