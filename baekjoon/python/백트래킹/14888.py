# 백트래킹 (Python3 통과, PyPy3도 통과)
import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)


# 순열 (Python3 시간초과 / PyPy3는 통과)
import sys
from itertools import permutations
from collections import deque

input = sys.stdin.readline
n = int(input())
seq = list(map(int, input().split()))

cal = ['+','-','*','//']
cal_input = list(map(int, input().split()))
cal_list=[]

for i in range(4):
    if cal_input[i] == 0:
        pass
    else:
        for j in range(cal_input[i]):
            cal_list.append(cal[i])

num_case = list(permutations(cal_list, len(cal_list)))
q=deque(num_case)

max_result = -1e9
min_result = -1e9

while q:
    now_list = q.popleft()
    result = seq[0]

    for i in range(1,len(seq)):
        if now_list[i-1]=='+':
            result += seq[i]
        elif now_list[i-1]=='-':
            result -= seq[i]
        elif now_list[i-1]=='*':
            result *= seq[i]
        elif now_list[i-1]=='//':
            if result < 0:
                result = -(abs(result)//seq[i])
            else:
                result = result//seq[i]
    
    max_result = max(max_result, result)
    min_result = min(min_result, result)

print(max_result)
print(min_result)
