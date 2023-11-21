n,m=map(int,input().split())

l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

results = len(set(l1) - set(l2)) + len(set(l2) - set(l1))
print(results)
