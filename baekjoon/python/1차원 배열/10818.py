import sys

n = int(sys.stdin.readline())
lst = list(map(int,sys.stdin.readline().rstrip().split()))
print(f'{min(lst)} {max(lst)}')