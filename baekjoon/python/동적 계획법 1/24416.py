while True:
    a,b,c = map(int, input().split())

    if min(a,b,c) <=0:
        print(f"w({a}, {b}, {c}) = 1")
        break

    n = max(a,b,c)

    if n < 20:
        n=20
        

    dp = [[[0]*(n+1)]*(n+1)]*(n+1)
    
    for i in range(0,a+1):
        for j in range(0,b+1):
            for k in range(0,c+1):
