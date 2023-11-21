k,n = map(int, input().split())

lst=[]
for _ in range(k):
    lst.append(int(input()))
    
start=1
end = max(lst) # 최대값에서 시작(범위)

while start<=end:
    mid=(start+end)//2
    
    _sum=0
    for item in lst:
        _sum+=(item//mid)

        # # 이부분이 없어야됨
        # # 최대값을 찾는 것이기 때문에 다른값도 조건을 만족 할 수 있음
        # # start값을 키워가면서 해봐야됨    
        # if _sum == n:
        #     print(mid)
        #     break

    # 다음 확인할 구역에 mid를 참여시킬 필요가 없어서 -1, +1을 함
    if _sum < n:
        end=mid-1
    else: # num > lst[mid]
        start=mid+1

print(end)