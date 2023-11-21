from collections import Counter

n, m = map(int, input().split())

lst = []
for _ in range(n):
    voca = input()
    if len(voca) >= m:
        lst.append(voca)

lst = Counter(lst)
print(list(lst))
