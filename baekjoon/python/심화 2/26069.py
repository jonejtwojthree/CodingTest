
# n = int(input())

# lst = ["ChongChong"]
# cnt=1
# for _ in range(n):
#     users = input().split()
#     if (users[0] in lst and users[1] not in lst):
#         cnt+=1
#         lst.append(users[1])
#     elif (users[1] in lst and users[0] not in lst):
#         cnt+=1
#         lst.append(users[0])
# print(cnt)


n = int(input())

dance = ["ChongChong"]

for _ in range(n):
    users = input().split()
    if users[0] in dance:
        dance.add(users[1])

    if users[1] in dance:
        dance.add(users[0])

print(len(dance))
