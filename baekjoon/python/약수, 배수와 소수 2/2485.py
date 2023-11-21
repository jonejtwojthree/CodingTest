import sys
import math

n = int(sys.stdin.readline())
lst = [ int(input()) for _ in range(n) ]
gcdd = math.gcd(*[ lst[i]-lst[i-1] for i in range(1,n)])

print(sum([ (lst[i]-lst[i-1])//gcdd-1 for i in range(1,n)]))
# print((lst[-1]-lst[0])//gcdd-1-(n-2))