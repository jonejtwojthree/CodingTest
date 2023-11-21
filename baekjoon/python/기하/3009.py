lx = []
ly = []
for _ in range(3):
    a, b = map(int, input().split())
    lx.append(a)
    ly.append(b)

lx.sort()
ly.sort()

x = y = 0
if lx[1] == lx[2]:
    x = lx[0]
else:
    x = lx[2]

if ly[1] == ly[2]:
    y = ly[0]
else:
    y = ly[2]

print(x, y)

# for i in range(3):
#     if x_nums.count(x_nums[i]) == 1:
#         x4 = x_nums[i]
#     if y_nums.count(y_nums[i]) == 1:
#         y4 = y_nums[i]
# print(x4, y4)
