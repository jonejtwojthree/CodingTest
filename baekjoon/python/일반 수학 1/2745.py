# string, jinsu = input().split()
# jinsu = int(jinsu)
# total = 0
# for i, s in enumerate(string):
#     if 65 <= ord(s) <= 90:
#         num = ord(s) - 65 + 10
#     else:
#         num = int(s)
#     n = len(string) - i - 1
#     total += num * pow(jinsu, n)
# print(total)

N, b = input().split()
ary = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

N = N[::-1]
result = 0

for i, n in enumerate(N):
    result += (int(b) ** i) * (ary.index(n))
print(result)
