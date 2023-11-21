n = int(input())

while n > 0:
    num = int(input())
    n -= 1

    quater = num // 25
    num = num - 25 * quater

    dime = num // 10
    num = num - 10 * dime

    nickel = num // 5
    num = num - 5 * nickel

    penny = num // 1
    num = num - 1 * penny

    print(f"{int(quater)} {int(dime)} {int(nickel)} {int(penny)}")
