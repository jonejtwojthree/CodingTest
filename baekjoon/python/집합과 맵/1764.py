n,m=map(int,input().split())

no_listen = []
for _ in range(n):
    no_listen.append(input())

no_see = []
for _ in range(m):
    no_see.append(input())

results = list(set(no_listen)&set(no_see))
results.sort()

print(len(results))
for result in results:
    print(result)

# a,b = map(int, input().split())

# nl = {input() for _ in range(a)}
# ns = {input() for _ in range(b)}

# nls = nl.intersection(ns)
# print(len(nls))
# for i in sorted(nls): # 정렬 해야함
#   print(i, end=' ')
  
