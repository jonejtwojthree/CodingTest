from bisect import bisect_left, bisect_right

n,x = map(int, input().split())

# array는 정렬된 상태여야됨(입력을 정렬된 상태로 입력)
array = list(map(int ,input().split()))

r_idx = bisect_right(array, x)
l_idx = bisect_left(array, x)

count = r_idx - l_idx
if count==0:
    print(-1)
else:
    print(count)