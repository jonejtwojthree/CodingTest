import sys

lst = []
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == b == 0:
        break
    lst.append(a + b)

for num in lst:
    print(num)
