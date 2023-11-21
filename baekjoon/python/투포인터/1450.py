import sys
input=sys.stdin.readline

n,c = map(int, input().split())
weights = list(map(int, input().split()))

weights.sort()

left=right=0

_sum=0
cnt=1
while left<right:
    if right <len(weights):    
        if _sum+weights[right] <= c:
            _sum+=weights[right]
            right+=1
            cnt+=1
        else:
            _sum-=weights[left]
            left+=1
    else:
        _sum-=weights[left]
        left+=1

print(cnt)