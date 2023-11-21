## lis dp로 하면 시간 초과
# n = int(input())
# lst = list(map(int, input().split()))


# dp = [1]*n

# for i in range(n):
#     for j in range(i):
#         if lst[j]<lst[i]:
#             dp[i]=max(dp[i], dp[j]+1)
# print(max(dp))

# 모르겟음

n = int(input())
lst = list(map(int, input().split()))

lis=[lst[0]]



for i in range(1,len(lst)):

    if lis[-1] < lst[i]:
        lis.append(lst[i])
    else:
        start=0
        end=len(lis)-1


        while start<=end:
            mid=(start+end)//2
            if lis[mid] < lst[i]:
                start=mid+1
            else:
                end=mid-1
        
        lis[start]=lst[i]
    print(lis)