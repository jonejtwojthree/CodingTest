# import itertools

# n,m = map(int, input().split())

# lst = [ i for i in range(1,n+1) ]
# results = list(itertools.combinations(lst,m))
# for result in results:
#     print(*result)

def f(lst, tmp, start):
    if len(tmp) == m:
        print(*tmp)
        return

    for i in range(start, len(lst)):
        tmp.append(lst[i])
        f(lst,tmp,i+1)
        tmp.pop()

n,m = map(int, input().split())

lst = [ i for i in range(1,n+1) ]
f(lst, [], 0)