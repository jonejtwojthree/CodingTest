n = int(input())

i = 1
while True:
    if n <= 3 * (i**2) - 3 * i + 1:
        print(i)
        break
    i += 1
