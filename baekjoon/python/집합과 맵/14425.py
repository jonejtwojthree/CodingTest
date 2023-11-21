# n,m = map(int, input().split())

# n_lst = []
# for _ in range(n):
#     n_lst.append(input())

# m_lst = []
# for _ in range(m):
#     m_lst.append(input())

# print(sum(map(lambda x: m_lst.count(x), n_lst)))

n,m = map(int, input().split())

n_lst = []
for _ in range(n):
    n_lst.append(input())

cnt=0
for _ in range(m):
    word = input()
    if word in n_lst:
        cnt+=1
print(cnt)