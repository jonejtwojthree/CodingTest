# n=int(input())
# lst = list(map(int, input().split()))
# lst.sort()

# _min=0
# size=len(lst)
# for i in range(len(lst)):
#     _min += (size-i)*lst[i]
# print(_min)

n=int(input())
lst = list(map(int, input().split()))
lst.sort()

for i in range(1,len(lst)):
    lst[i] += lst[i-1]

print(lst)
print(sum(lst))
