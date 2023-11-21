import sys
n,m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))


# 누적합을 통해서 m으로 나눈 나머지를 인덱스로 하여 갯수를 저장
numRemainder = [0]*m

_sum=0
for i in range(n):
    _sum += lst[i]
    numRemainder[_sum%m]+=1

# 나머지가 0인것은 2개를 뽑을 필요가 없음
cnt=numRemainder[0]

# 나머지가 같은것을 2개 뽑으면 됨 // 나머지가 같게 나온 원흉을 공유하니깐
for num in numRemainder:
    #Combination
    cnt += num*(num-1)//2

print(cnt)