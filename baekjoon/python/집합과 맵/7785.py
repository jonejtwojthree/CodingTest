n = int(input())

enter_dic = {}
for _ in range(n):
    name, stat= input().split()
    if stat=="enter":
        enter_dic[name] = True
    else:
        enter_dic.pop(name)
        # del enter_dic[name]

results = sorted(enter_dic.keys(), reverse=True)

for key in results:
    print(key)
