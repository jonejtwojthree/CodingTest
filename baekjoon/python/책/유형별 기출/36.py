str1 = input()
str2 = input()

n=len(str1)
m=len(str2)

dp = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(n+1):
    dp[i][0]=i
for j in range(m+1):
    dp[0][j]=j

for i in range(1,n+1):
    for j in range(1,m+1):
        if str1[i-1]==str2[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
print(dp[-1][-1])