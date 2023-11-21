while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break

    lst = sorted([a, b, c])
    if lst[0] + lst[1] <= lst[2]:
        print("Invalid")
    else:
        if a == b == c:
            print("Equilateral")
        elif a == b or b == c or c == a:
            print("Isosceles")
        elif a != b and b != c and c != a:
            print("Scalene")
