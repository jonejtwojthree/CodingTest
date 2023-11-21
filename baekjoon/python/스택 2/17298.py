import sys

input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))

# A의 0번째 인덱스 삽입
stack=[0]
NGE = [-1]*n
for i in range(1, n):
    while stack and A[stack[-1]] < A[i]:
        NGE[stack.pop()]=A[i]
    stack.append(i)
print(*NGE)