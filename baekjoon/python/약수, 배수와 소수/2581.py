def isSosu(num):
    if num == 1:
        return False
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            return False
    return True


n1 = int(input())
n2 = int(input())

sum = 0
min = 0

for num in range(n2, n1 - 1, -1):
    if isSosu(num):
        sum += num
        min = num
if sum == 0:
    print(-1)
else:
    print(sum)
    print(min)
