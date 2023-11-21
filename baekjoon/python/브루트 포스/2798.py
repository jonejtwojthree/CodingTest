import itertools

n, m = map(int, input().split())
lst = list(map(int, input().split()))

combi = list(itertools.combinations(lst, 3))
print(max(filter(lambda x: x <= m, map(sum, combi))))
