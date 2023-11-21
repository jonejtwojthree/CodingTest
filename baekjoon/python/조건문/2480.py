from collections import Counter

a,b,c = map(int, input().split())
counter = Counter([a,b,c])

print(counter)
print(counter.most_common(1))
print(counter.most_common(2))
print(counter.most_common(3))

money = 10000 + counter.most_common(3)[0][0]*1000 if len(counter.most_common(3)) == 1 else 1000 + counter.most_common(3)[0][0]*100  if len(counter.most_common(3)) == 2 else max(a,b,c)*100
print(money)


# d1, d2, d3 = map(int, input().split())

# if d1 == d2 == d3:
#     print(10000 + d1 * 1000)
# elif d1 == d2 or d1 == d3 or d2 == d3:
#     print(1000 + d1 * 100) if d1 == d3 else print(1000 + d2 * 100)
# else:
#     print(max(d1, d2, d3) * 100)