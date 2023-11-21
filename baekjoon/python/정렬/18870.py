import sys
n = int(input())

numbers = list(map(int, sys.stdin.readline().rstrip().split()))

numset = set(numbers)
a = list(numset)
a.sort()

# counter와 다름
# 오름차순으로 정렬된 a를 통해 인덱스의 값이 나보다 작은값의 개수가 됨
numdict = {}
for i in range(len(a)):
    numdict[a[i]] = i

for i in numbers:
    print(numdict[i], end=' ')

