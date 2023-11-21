# 첫번째 집은 무조건 설치 하고
# 이분 탐색의 mid값을 띄어서 짓는 것으로 정험
# d즉 이분탐색의 start, end, mid는 공유기 거리
# start: 최소 거리
# end: 최대 거리
# mid: 띄어서 지을 거리?

# 모르갰다

n,c = map(int, input().split())

lst=[]
for _ in range(n):
    lst.append(int(input()))
lst.sort()

start=1
end = lst[-1]-lst[0]

result=0
while start<=end:
    mid=(start+end)//2 # 현재 공유기 거리
    cur=lst[0] # 시작지점에 공유기 박고 시작
    count=1 # 시작지점에 공유기 박고하니까 1개부터 시작

    _sum=0
    for i in range(1,len(lst)):
        if lst[i] >= cur+mid:
            count+=1
            cur=lst[i] # cur+mid가 아니라 lst[i]임 // 집에다 지어야 되서
            
    if count >= c: # 공유기 대수를 많이 추가해서 사이 간격을 늘려서 좁힘
        start=mid+1
        result=mid # 사이 거리
    else: # 공유기 대수를 못채워서 공유기 사이 간격을 줄임
        end=mid-1

print(result)