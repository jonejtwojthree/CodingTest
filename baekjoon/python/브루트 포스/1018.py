# m, n = map(int, input().split())

# chess = []
# min_cnt = 1000000000
# for _ in range(m):
#     chess.append(input())

# for y_start in range(m - 8 + 1):
#     for x_start in range(n - 8 + 1):
#         c1 = chess[y_start][x_start]
#         c2 = "B" if c1 == "W" else "W"

#         cnt1 = 0
#         for i in range(0, 8, 2):
#             cnt1 += chess[y_start + i][x_start : x_start + 8 : 2].count(c2) + chess[
#                 y_start + i
#             ][x_start + 1 : x_start + 8 : 2].count(c1)

#         for i in range(1, 8, 2):
#             cnt1 += chess[y_start + i][x_start : x_start + 8 : 2].count(c1) + chess[
#                 y_start + i
#             ][x_start + 1 : x_start + 8 : 2].count(c2)

#         c1, c2 = c2, c1
#         cnt2 = 0
#         for i in range(0, 8, 2):
#             cnt2 += chess[y_start + i][x_start : x_start + 8 : 2].count(c2) + chess[
#                 y_start + i
#             ][x_start + 1 : x_start + 8 : 2].count(c1)

#         for i in range(1, 8, 2):
#             cnt2 += chess[y_start + i][x_start : x_start + 8 : 2].count(c1) + chess[
#                 y_start + i
#             ][x_start + 1 : x_start + 8 : 2].count(c2)

#         cnt = min(cnt1, cnt2)
#         if cnt < min_cnt:
#             min_cnt = cnt
# print(min_cnt)

N, M = map(int, input().split())
original = []
count = []

for _ in range(N):
    original.append(input())

for a in range(N - 7):
    for b in range(M - 7):
        index1 = 0
        index2 = 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if original[i][j] != "W":
                        index1 += 1
                    if original[i][j] != "B":
                        index2 += 1
                else:
                    if original[i][j] != "B":
                        index1 += 1
                    if original[i][j] != "W":
                        index2 += 1
        count.append(min(index1, index2))

print(min(count))
