import sys
n = int(sys.stdin.readline())
for _ in range(n):
    str = sys.stdin.readline().rstrip()
    print(f'{str[0]}{str[-1]}')