lst = [input() for _ in range(5)]

for j in range(15):
    for i in range(5):
        try:
            print(lst[i][j], end="")
        except:
            pass
