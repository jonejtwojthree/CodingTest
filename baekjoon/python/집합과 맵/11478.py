# import itertools

# string = input()

# cnt=0

# for size in range(len(string)):
#     lst = []
#     for i in range(len(string)-size):
#         lst.append(string[i:i+size+1])
#     cnt += len(set(lst))

# print(cnt)

import itertools

string = input()

cnt=0

_set = set()
for size in range(len(string)):
    lst = []
    for i in range(len(string)-size):
        _set.add(string[i:i+size+1])
    
print(len(_set))