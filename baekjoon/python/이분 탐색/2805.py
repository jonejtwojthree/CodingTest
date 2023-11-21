n,m = map(int, input().split())

lst=list(map(int, input().split()))
    
start=1
end = max(lst) # 최대값에서 시작(범위)

while start<=end:
    mid=(start+end)//2
    
    _sum = sum(filter(lambda x: x>0, map(lambda x: x-mid, lst)))

    # 다음 확인할 구역에 mid를 참여시킬 필요가 없어서 -1, +1을 함
    if _sum < m:
        end=mid-1
    else: # num > lst[mid]
        start=mid+1

print(end)