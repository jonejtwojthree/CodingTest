from collections import Counter
import sys
input = sys.stdin.readline

n = input().rstrip()

result=0
for x in n:
    x = int(x)
    if x<=1 or result <=1:
        result += x
    else:
        result *= x

    print(result)
