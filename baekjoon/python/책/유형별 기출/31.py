for t in range(int(input())):
    n,m=map(int, input().split())
    array = list(map(int, input().split()))

    dp=[]
    index=0
    # dp를 0으로 초기화 안하고 graph랑 똑같은 값으로 초기화
    for i in range(n):
        dp.append(array[index:index+m])
        index+=m

    for j in range(1,m):
        for i in range(n):
            # 맨위
            if i==0:
                left_up=0
            else:
                left_up = dp[i-1][j-1]
            
            # 맨아래
            if i==n-1:
                left_down=0
            else:
                left_down=dp[i+1][j-1]
            
            left = dp[i][j-1]
            dp[i][j] = dp[i][j]+max(left, left_down, left_up)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    print(result)

