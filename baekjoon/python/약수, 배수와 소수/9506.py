while True:
    num = int(input())
    if num == -1:
        break

    lst = [1]
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            lst.append(i)
    if sum(lst) == num:
        s = " + ".join(map(str, lst))
        print(f"{str(num)} = {s}")
    else:
        print(f"{num} is NOT perfect.")
