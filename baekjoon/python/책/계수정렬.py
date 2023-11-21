# 선택 정렬
# O(N^2)
# 정렬되있을 필요 없음

from collections import Counter

array=[3,4,3,-1,5,5,5,1,1,1,5,1,-2]

dic=dict()

for num in array:
    try:
        dic[str(num)]+=1
    except:
        dic[str(num)]=1

keys = list(map(int, dic.keys()))
keys.sort()

for key in keys:
    for _ in range(dic[str(key)]):
        print(key, end=' ')
    print()