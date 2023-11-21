#LIS (Longest Increasing Subsequence)
# 최장 증가 부분 수열
# 가장 긴 증가하는 부분 수열
# 오름차순으로 정렬된 가장 긴 부분

# A를 오름차순으로 정렬하고 
# B를 LIS해서 n으로 빼면 없어져야될 최소한의 개수가 나옴

import sys
input = sys.stdin.readline

n = int(input())
array = list(map(int, input().split()))
array.reverse()

dp = [1]*n

for i in range(1,n):
    for j in range(0,i):
        if array[j]<array[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(n-max(dp))