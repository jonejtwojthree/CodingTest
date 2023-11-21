import sys
n=int(input())

lst=[0]
for _ in range(n):
    lst.append(int(input()))

if n==1 or n==2:
    print(sum(lst))
    sys.exit(0)
dp = [0]*(n+1)

dp[1]=lst[1]
dp[2]=lst[1]+lst[2]

for i in range(3,n+1):
    # i번째 계단에 올라왔을때 가장 높은 가치(i번째에 오른상태)(와인처럼 안먹어도 되는거 아니고)
    dp[i]=max(dp[i-2]+lst[i], dp[i-3]+lst[i-1]+lst[i])


print(dp[-1])