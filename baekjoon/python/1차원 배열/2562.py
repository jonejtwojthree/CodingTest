import sys

lst = []
for _ in range(9):
    lst.append(int(sys.stdin.readline()))
print(f'{max(lst)} {lst.index(max(lst))+1}')