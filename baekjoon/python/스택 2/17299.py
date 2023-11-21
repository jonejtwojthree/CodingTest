# # 시간 초과
# import sys
# from collections import Counter

# input = sys.stdin.readline

# n = int(input())
# A = list(map(int, input().split()))
# counter = Counter(A)

# NGF=[-1]*n

# for i in range(n):
#     for j in range(i+1,n):
#         if counter[A[i]] < counter[A[j]]:
#             NGF[i]=A[j]
#             break
    
# print(*NGF)


import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
counter = Counter(A)

NGF=[-1]*n

# A의 0번째 인덱스
stack=[0]
for i in range(1,n):
    while stack and counter[A[stack[-1]]] < counter[A[i]]:
        NGF[stack.pop()]=A[i]
    stack.append(i)
print(*NGF)

