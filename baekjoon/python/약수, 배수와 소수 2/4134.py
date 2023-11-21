import sys
import math

def isSosu(x):
    for i in range(3, int(math.sqrt(x))+1,2): # 범위를 줄여줌
        if x % i == 0:
            return False
    return True

n = int(input())
_max = sys.maxsize
for _ in range(n):
    num = int(input())
    if num==0 or num==1:
        print(2)
        continue
    elif num==2:
        print(num)
        continue

    if num%2==0:
        num+=1
    for i in range(num, _max,2): # 범위를 줄여줌
        if isSosu(i):
            print(i)
            break


# import sys
# import math

# def isSosu(x):
#     if x == 0 or x == 1:
#         return False
#     for i in range(2, int(math.sqrt(x))+1): # 범위를 줄여줌
#         if x % i == 0:
#             return False
#     return True

# n = int(input())
# _max = sys.maxsize
# for _ in range(n):
#     num = int(input())

#     for i in range(num, _max):
#         if isSosu(i):
#             print(i)
#             break