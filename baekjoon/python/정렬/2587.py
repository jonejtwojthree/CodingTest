lst=[]
for _ in range(5):
    lst.append(int(input()))

lst.sort()
print(sum(lst)//len(lst))
print(lst[len(lst)//2])