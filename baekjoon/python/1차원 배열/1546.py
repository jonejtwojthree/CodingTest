import sys

n = int(input())

lst = list(map(int, sys.stdin.readline().rstrip().split()))
print(lst)
max_score = max(lst)
print(sum(map(lambda x: x/max_score*100, lst))/n)