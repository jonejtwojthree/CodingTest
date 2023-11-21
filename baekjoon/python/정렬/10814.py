n = int(input())

lst = []
for _ in range(n):
    age, name = input().split()
    lst.append([int(age), name])

lst.sort(key=lambda x: x[0])

for l in lst:
    print(*l)