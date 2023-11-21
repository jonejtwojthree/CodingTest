import sys

str = sys.stdin.readline().rstrip()
lst = [-1]*26

for i, x in enumerate(str):
    idx = ord(x)-97
    if lst[idx] == -1:
        lst[idx]=i
print(*lst)