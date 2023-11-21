#LIS (Longest Increasing Subsequence)
# 최장 증가 부분 수열
# 가장 긴 증가하는 부분 수열
# 오름차순으로 정렬된 가장 긴 부분

# A를 오름차순으로 정렬하고 
# B를 LIS해서 n으로 빼면 없어져야될 최소한의 개수가 나옴

import sys
input = sys.stdin.readline

N = int(input())
edge = [list(map(int, input().split())) for _ in range(N)]

# 첫 번째 전봇대 기준 오름차순 정렬
edge = sorted(edge, key = lambda x: x[0])

# LIS
LIS = [1]*N

for idx in range(1, N):
    for i in range(idx):
        if edge[i][1] < edge[idx][1]:
            LIS[idx] = max(LIS[idx], LIS[i] + 1)
print(edge)
print(LIS)
print(N - max(LIS))