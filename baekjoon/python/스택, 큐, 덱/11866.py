from sys import stdin

N, K = map(int,stdin.readline().split())
index = 0
array = list(range(1,N+1))
result = []

# while len(array) != 0: # 리스트 수가 0이 아니면 반복
#     print(index, array)
#     index += (K-1)
#     index = index % len(array)
#     result.append(array.pop(index))

# ## 문자
# print("<",end="")
# for i in range(N-1):
#     print(result[i],end=", ")
# print(result[N-1], end = "")
# print(">",end="") 

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


from collections import deque
from sys import stdin

N, K = map(int,stdin.readline().split())
index = 0
array = list(range(1,N+1))
result = []

queue = deque(array)
step=K-1
print("<", end='')
while len(queue)>1:
    while step>0:
        queue.append(queue.popleft())
        step-=1
    print(f"{queue.popleft()}", end=', ')
    step=K-1
print(f"{queue[0]}>")
