import sys
import math

a1, b1 = map(int, sys.stdin.readline().split())
a2, b2 = map(int, sys.stdin.readline().split())

top = (a1*b2+a2*b1)
bottom = b1*b2

tb_gcd = math.gcd(top, bottom)

print(top//tb_gcd, bottom//tb_gcd)