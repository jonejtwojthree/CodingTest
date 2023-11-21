import sys
sys.stdin.readline()
str = sys.stdin.readline().rstrip()

print(sum(map(int, [*str])))