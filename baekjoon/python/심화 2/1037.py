n = int(input())

# 해당 약수를 모두 리스트에 줌
lst = list(map(int, input().split()))

lst.sort()
print(lst[0] * lst[-1])
