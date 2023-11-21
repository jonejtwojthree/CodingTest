from collections import Counter
import sys
input = sys.stdin.readline

data = input().rstrip()

zero=one=0

if data[0]=='0':
    one+=1
else:
    zero+=1
    
for i in range(len(data)-1):
    if data[i] != data[i+1]:
        if data[i+1]=='0':
            one+=1
        else:
            zero+=1
            
print(min(zero, one))