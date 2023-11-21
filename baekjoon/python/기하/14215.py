a, b, c = map(int, input().split())

lst = sorted([a, b, c])
if lst[0] + lst[1] > lst[2]:
    print(sum(lst))
else:
    print(2 * (lst[0] + lst[1]) - 1)
