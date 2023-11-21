n = int(input())
lst = list(map(int, input().split()))

lst.sort()

m=int(input())
for num in map(int, input().split()):
    
    start=0
    end = len(lst)-1
    flag=0
    cnt=0

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


    if flag==1:
        tmp=mid
        while tmp > -1 and lst[tmp]==num:
            tmp-=1
            cnt+=1
        
        tmp=mid
        while tmp <len(lst) and lst[tmp]==num:
            tmp+=1
            cnt+=1
        
        cnt-=1 #while문 2번 해서 1 빼야함

    print(cnt, end=' ')


# Counter로도 해결할 수 있음

from collections import Counter

n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

count = Counter(n_arr)

for m_data in m_arr:
  if m_data in count:
    print(count[m_data], end=' ')
  else:
    print(0, end=' ')


# dict으로 해결(Counter와 같은 원리)
n = int(input())
n_cards = list(input().split())

n_dict = {}

for n_card in n_cards:
    try:
        n_dict[n_card]+=1
    except:
        n_dict[n_card]=1

m = int(input())
m_cards = list(input().split())

for m_card in m_cards:
    try:
        print(n_dict[m_card], end=' ')
    except:
        print(0, end=' ')