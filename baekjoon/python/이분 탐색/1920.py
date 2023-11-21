n = int(input())
lst = list(map(int, input().split()))

lst.sort()
lst.insert(0,0)

m=int(input())
for num in map(int, input().split()):
    
    start=1
    end = len(lst)-1
    flag=0
    
    while start<=end:
        mid=(start+end)//2
        
        if lst[mid]==num:
            flag=1
            break
        # 다음 확인할 구역에 mid를 참여시킬 필요가 없어서 -1, +1을 함
        elif num < lst[mid]:
            end=mid-1
        else: # num > lst[mid]
            start=mid+1
    print(flag)