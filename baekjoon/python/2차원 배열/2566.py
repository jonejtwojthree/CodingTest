import sys

maxi = -1
row = -1
col = -1

for i in range(9):
    lst = list(map(int, sys.stdin.readline().split()))
    row_max = max(lst)
    if row_max > maxi:
        maxi = row_max
        row = i
        col = lst.index(maxi)

print(maxi)
print(f"{row+1} {col+1}")
