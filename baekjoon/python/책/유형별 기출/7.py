from collections import Counter
import sys
input = sys.stdin.readline

data = input().rstrip()

mid=len(data)//2+1

if sum(map(int, data[:mid])) == sum(map(int, data[mid:])):
    print("LUCKY")
else:
    print("READY")