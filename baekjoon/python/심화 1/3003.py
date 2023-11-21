import sys

chess = [1, 1, 2, 2, 2, 8]
lst = list(map(int, sys.stdin.readline().split()))
print(*[i - j for i, j in zip(chess, lst)])
