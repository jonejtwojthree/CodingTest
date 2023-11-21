import sys
import math

# def isSosu(x):
#     if x==0 or x==1:
#         return False
#     if x==2:
#         return True
    
#     for i in range(2, int(math.sqrt(x))+1): # 범위를 줄여줌
#         if x % i == 0:
#             return False
#     return True

# a,b = map(int, input().split())

# for i in range(a, b+1): # 범위를 줄여줌
#     if isSosu(i):
#         print(i)
        
a,b = map(int, input().split())

sosu=[True for _ in range(b+1)]
sosu[0]=sosu[1]=False
result=[]
for i in range(2, int(math.sqrt(b)+1)):
    if sosu[i]:
        result.append(i)
        for j in range(2*i,b+1,i):
            sosu[j]=False
print(*result)