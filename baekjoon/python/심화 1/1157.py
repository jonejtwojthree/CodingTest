# from collections import Counter

# string = input().upper()
# counter = Counter(string)

# most = counter.most_common(2)

# try:
#     if most[0][1] == most[1][1]:
#         print("?")
#     else:
#         print(most[0][0])
# except:
#     print(most[0][0])

string = input().upper()
words = list(set(string))
count_lst = []
for x in words:
    cnt = string.count(x)
    count_lst.append(cnt)

if count_lst.count(max(count_lst)) > 1:
    print("?")
else:
    print(words[(count_lst.index((max(count_lst))))])
