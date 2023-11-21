n = int(input())

lst = []
for _ in range(n):
    word = input()
    if word not in lst:
        lst.append(word)

lst.sort(key=lambda x: (len(x), x))
for l in lst:
    print(l)