# n, m = map(int, input().split())
# lst = [i for i in range(n+1)]

# for _ in range(m):
#     i, j = map(int, input().split())
#     for k in range((j-i)//2+1):
#         tmp = lst[i+k]
#         lst[i+k] = lst[j-k]
#         lst[j-k] = tmp
# print(*lst[1:])


n, m = map(int, input().split())
lst = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    tmp = lst[i:j+1]
    tmp.reverse()
    lst[i:j+1]=tmp
print(*lst[1:])
