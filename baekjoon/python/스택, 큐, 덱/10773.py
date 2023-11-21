import sys

n = int(sys.stdin.readline())

stack=[]
for _ in range(n):
    num = int(sys.stdin.readline())
    if num==0:
        try:
            stack.pop()
        except:
            pass
    else:
        stack.append(num)

print(stack)
print(sum(stack))