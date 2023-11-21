import sys

dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

sum=0
str = list(sys.stdin.readline().rstrip())
for ch in str:
    for i, di in enumerate(dial):
        if ch in di:
            sum+=(i+3)
print(sum)