import sys

input = sys.stdin.readline

n,m = map(int, input().split())
array =list(map(int, input().split()))

start=0
end=max(array)

result=0
while start<=end:
    mid = (start+end)//2
    _sum = sum(filter(lambda x: x>0, map(lambda x: x-mid, array)))

    if _sum >= m:
        result=mid
        start = mid+1
    else:
        end = mid-1
print(result)