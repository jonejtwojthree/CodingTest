import sys

lst = [True]*31
for _ in range(28):
    num = int(input())
    lst[num]=False

for idx, flag in  enumerate(lst[1:]):
    if flag:
        print(idx+1)
