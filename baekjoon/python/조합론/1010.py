def f(n):
    if n == 0:
        return 1
    else:
        return n * f(n - 1)


n = int(input())

for _ in range(n):
    k, n = map(int, input().split())
    print(int(f(n) / ((f(k)) * f(n - k))))
