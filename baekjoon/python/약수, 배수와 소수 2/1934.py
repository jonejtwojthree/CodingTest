import math
import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a,b = map(int, sys.stdin.readline().split())
    print(int(math.lcm(a,b)))


def GCD(a,b):
  if a%b==0:
    return b
  else:
    return GCD(b,a%b)

def LCM(a,b):
  gcd = GCD(a,b)
  return int((a*b)/gcd)