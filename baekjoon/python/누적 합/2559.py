import sys
n,m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))

# dp[k]: sum(lst[1] ~ lst[k])
# dummy 인덱스 사용

dp = [0]*(n+1)
for i in range(1, n+1):
    dp[i] = dp[i-1]+lst[i-1]

tmp = []
for i in range(1, n+1-m+1):
    tmp.append(dp[i+m-1]-dp[i-1])
print(max(tmp))


# N, K = map(int, input().split())
# temp_list = list(map(int, input().split()))

# part_sum = sum(temp_list[:K])
# answer = part_sum

# for i in range(N-K) :
#   part_sum += temp_list[i+K] - temp_list[i]
#   if answer < part_sum :
#     answer = part_sum

# print(answer)