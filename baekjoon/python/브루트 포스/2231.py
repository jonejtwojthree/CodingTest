n = int(input())

for num in range(1, n + 1):
    total = sum(map(int, list(str(num)))) + num
    if n == total:
        print(num)
        break
    if num == n:
        print(0)
        break
