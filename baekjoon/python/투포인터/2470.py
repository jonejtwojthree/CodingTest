import sys
input=sys.stdin.readline

n=int(input())
lst=list(map(int, input().split()))
lst.sort() # 정렬하고 투포인터 사용

left=0
right=len(lst)-1

_max=sys.maxsize
answer=None
# print(lst)
while left<right:
    # print(left, right, abs(lst[right]+lst[left]))
    _sum = lst[right]+lst[left]
    if abs(_sum) < _max: 
        answer=(lst[left], lst[right])
        _max=abs(_sum)

    # 더한값이 0보다 작으면 left+1 크면 right-1로 내가 정함
    if _sum < 0:
        # left+=1
        right-=1
    else:
        # right-=1    
        left+=1
print(*answer)


# # 시간 초과
# import itertools
# import sys
# n=int(input())
# lst=list(map(int, input().split()))

# combi = itertools.combinations(lst, 2)

# items=None
# result=sys.maxsize

# for i,j in combi:
#     abb=abs(i+j)
#     if abb<result:
#         result = abb
#         items = (i,j)

# print(items)