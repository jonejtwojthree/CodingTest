# 짜잘한거 쳐내고 큰거 한방
num = int(input())
count = 0

while num >= 0:
    if num % 5 == 0:
        count += int(num // 5)
        print(count)
        break

    num -= 3
    count += 1

else:
    print(-1)

# import sys

# n = int(input())
# max_int = sys.maxsize
# min = max_int

# for x in range(max_int):
#     if 5 * x > n:
#         break

#     for y in range(max_int):
#         result = 5 * x + 3 * y
#         if result == n:
#             if x + y < min:
#                 min = x + y
#             break
#         elif result > n:
#             break

# print(min if min != max_int else -1)
