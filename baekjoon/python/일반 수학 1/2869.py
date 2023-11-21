# a, b, v = map(int, input().split())

# current = 0
# days = 0
# while True:
#     days += 1
#     if current + a >= v:
#         break

#     current += a - b
# print(days)


import math

a, b, v = map(int, input().split())
print(int(math.ceil((v - a) / (a - b))) + 1)
