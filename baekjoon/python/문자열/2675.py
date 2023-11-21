import sys
n = int(sys.stdin.readline())
for _ in range(n):
    n,str = sys.stdin.readline().rstrip().split()
    n=int(n)
    s=''
    for ch in str:
      s+=(ch*n)
    print(s)  