from sys import stdin


while True:
    graph = list(map(int, stdin.readline().split()))

    # 0이 입력되면 반복문을 종료합니다.
    if graph[0] == 0:
        break
    
    graph=graph[1:]
    # 스택과 최대 직사각형 넓이를 저장할 변수를 초기화합니다.
    stack = []
    max_result = min(graph)*(len(graph))

    for height in graph:
        if not stack or height > stack[-1]:
            stack.append(height)
            continue
        
        w=1
        while stack and height < stack[-1]:
            h = stack.pop()
            max_result = max(max_result, w*h)
            w+=1
        stack.append(height)

    w=1
    while stack:
        h=stack.pop()
        max_result=max(max_result, w*h)
        w+=1

    # 최대 직사각형 넓이를 출력합니다.
    print(max_result)