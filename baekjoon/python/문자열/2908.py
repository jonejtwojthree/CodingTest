import sys
a,b = sys.stdin.readline().split()

# num1 = int(num1[::-1])  # [::-1] : 역순
# num2 = int(num2[::-1])

a = list(a)
a.reverse()

b = list(b)
b.reverse()

a = int(''.join(a))
b = int(''.join(b))

print(a if a> b else b)