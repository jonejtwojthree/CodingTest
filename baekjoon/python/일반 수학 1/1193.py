# 1/1
# 1/2 2/1
# 3/1 2/2 1/3
# 1/4 2/3 3/2 4/1
# 5/1 4/2 3/3 2/4 1/5
# ...

# 홀수 1, 3, 5
# 짝수 2, 4, 6


x = int(input())

line = 1
while x > line:
    x -= line
    line += 1

if line % 2 == 0:
    print(f"{x}/{line-x+1}")
else:
    print(f"{line-x+1}/{x}")
