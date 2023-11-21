from sys import stdin

N = int(stdin.readline())
lst = list(map(int, input().split()))

index = 0
array = list(range(1,N+1))
results = []
i=0

results.append(array.pop(index))
while len(array) != 0: # 리스트 수가 0이 아니면 반복
    print(array)
    print(f'계산전 인덱스: {index}')
    
    k = lst[i]
    i+=1 
    print(f'k: : {k}')
    if k<0:
        index += k
        index = index%len(array)
    else:
        index += (k-1)
        index = index%len(array)
    print(f'계산후 인덱스: {index}')
    results.append(array.pop(index))
    print(results)
    

print(*results)

# import sys
# from collections import deque

# queue = deque()
# result = []

# n, k = map(int, sys.stdin.readline().split());

# for i in range(1, n+1):
#     queue.append(i)

# while queue:
#     for i in range(k-1):
#         queue.append(queue.popleft()) # 다시 넣기
#     result.append(queue.popleft()) # results로 넣기

# print("<", end='')
# print(', '.join(map(str,result)), end='')
# print(">")


