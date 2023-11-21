#LCS(Longest Common Subsequence) 최장 공통 부분 수열
# 두 수열의 부분 수열이 되는 부분수열 중 가장 긴 수열

import sys
read =  sys.stdin.readline
word1, word2 = sys.stdin.readline().rstrip(), sys.stdin.readline().rstrip()

w1, w2 = len(word1), len(word2)
dp=[[0]*(w2+1) for _ in range(w1+1)]

for i in range(1,w1+1):
    for j in range(1,w2+1):
        if word1[i-1] == word2[j-1]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j], dp[i][j-1])

print(dp)


# LIS

# LDS

# LCS
