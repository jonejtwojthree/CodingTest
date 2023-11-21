n=int(input())
dp=[[ 0 for _ in range(n) ] for _ in range(n)]
lst=[]

for i in range(n):
    lst.append(list(map(int, input().split())))

for i in range(n):
    size = len(lst[i])
    for j in range(size):
        if i==0:
            dp[i][j]=lst[i][j]
            break

        if j==0:
            dp[i][j]=dp[i-1][j]+lst[i][j]
        else:
            dp[i][j]=max(dp[i-1][j-1], dp[i-1][j])+lst[i][j]
print(max(dp[-1]))



# lst를 dp로 활용함
n=int(input())
d=[]
for i in range(n):
  d.append(list(map(int, input().split())))

for i in range(1,n):
  for j in range(len(d[i])):
    if j==0:
      d[i][j]=d[i][j]+d[i-1][j]
    elif j==len(d[i])-1: 
      d[i][j]=d[i][j]+d[i-1][j-1]
    else:
      d[i][j]=max(d[i-1][j-1],d[i-1][j])+d[i][j]
print(max(d[n-1]))