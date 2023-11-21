n=20

dp = [[[1 for _ in range(n+1)] for _ in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if i<j<k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1]-dp[i-1][j-1][k-1]

while True:
    a,b,c = map(int, input().split())
    
    if a==b==c==-1:
        break
    else:
        if a>20 or b>20 or c>20:
            print(f"w({a}, {b}, {c}) = {dp[20][20][20]}")
        elif a<=0 or b<=0 or c<=0:
            print(f"w({a}, {b}, {c}) = {1}")        
        else:
            print(f"w({a}, {b}, {c}) = {dp[a][b][c]}")


# 재귀와 dp의 혼합
# dp가 존재하면 리턴 없으면 재귀함수 호출

import sys
input = sys.stdin.readline

def w(a, b, c):
    if a <= 0 or b<= 0 or c<=0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if dp[a][b][c]:
        return dp[a][b][c]
    if a<b<c:
        dp[a][b][c] = w(a,b,c-1)+w(a,b-1,c-1)-w(a, b-1, c)
        return dp[a][b][c]
    dp[a][b][c] = w(a-1, b, c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return dp[a][b][c]

dp = [[[0]*(21) for _ in range(21)] for _ in range(21)]
# 0~20까지므로

while 1:
    a, b, c = map(int, input().split())
    if a==-1 and b==-1 and c==-1:
        break
    print(f'w({a}, {b}, {c}) = {w(a,b,c)}')


