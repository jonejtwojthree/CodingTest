import itertools

n,m = map(int, input().split())

lst = [ i for i in range(1,n+1) ]
results = list(itertools.combinations_with_replacement(lst,m))
for result in results:
    print(*result)

# def f(lst, tmp, start):
#     if len(tmp) == m:
#         print(*tmp)
#         return

#     for i in range(start, len(lst)):
#         tmp.append(lst[i])
#         f(lst,tmp,i)
#         tmp.pop()

# n,m = map(int, input().split())

# lst = [ i for i in range(1,n+1) ]
# f(lst, [], 0)