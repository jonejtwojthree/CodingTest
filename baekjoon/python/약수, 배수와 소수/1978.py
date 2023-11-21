n = int(input())
cnt = 0
lst = list(map(int, input().split()))
for num in lst:
    if num == 1:
        cnt += 1
        continue
    for i in range(2, num // 2):
        if num % i == 0:
            cnt += 1
            break
print(len(lst) - cnt)
