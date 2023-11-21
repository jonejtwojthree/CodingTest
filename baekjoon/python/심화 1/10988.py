# string = input()

# size = len(string)
# flag = True
# for i in range(size // 2):
#     if string[i] != string[size - i - 1]:
#         flag = False
#         break
# if flag:
#     print(1)
# else:
#     print(0)

a = input()
print(1 if a == a[::-1] else 0)
