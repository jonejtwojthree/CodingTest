def calc():
    for i in range(-999, 1000):
        for j in range(-999, 1000):
            if a * i + b * j == c and d * i + e * j == f:
                print(f"{i} {j}")
                return


a, b, c, d, e, f = map(int, input().split())
calc()

# y = (a * f - c * d) / (a * e - b * d)
# x = (c - b * y) / a

# 수식에서 ad-bc 부분
k = a * e - b * d

# x, y 행렬곱 식을 풀어서 넣음
print((e * c - b * f) // k, (-c * d + a * f) // k)
