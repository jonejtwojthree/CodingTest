## 시간초과
# import sys

# input = sys.stdin.readline
# string = input().rstrip()
# explode = input().rstrip()

# while explode in string:
#     string = string.replace(explode, "")
# if len(string)>0:
#     print(string)
# else:
#     print("FRULA")

# 시간 초과 방지를 위해서 stack으로 문제를 풀었고
# 마지막 값이 같을때만 제대로 검사를 함
# del문을 사용하여 빠르게 삭제

# import sys

# input = sys.stdin.readline
# string = input().rstrip()
# explode = input().rstrip()

# stack=[]
# explode_length = len(explode)
# lastChr=explode[-1]

# for ch in string:
#     stack.append(ch)

#     while stack[-1]==lastChr and ''.join(stack[-explode_length:]) == explode:
#         del stack[-explode_length:]
# if len(stack)>0:
#     print(''.join(stack))
# else:
#     print("FRULA")