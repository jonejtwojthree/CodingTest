import sys

n, x = map(int, sys.stdin.readline().split())
lst = list(map(int,sys.stdin.readline().rstrip().split()))
result = list(filter(lambda num: num<x, lst))

print(*result)