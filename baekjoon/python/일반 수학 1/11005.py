N, b = map(int, input().split())
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0

s = ""

while N > 0:
    s += ary[N % b]
    N //= b
print(s[::-1])
