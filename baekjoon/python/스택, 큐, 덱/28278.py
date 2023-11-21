n = int(input())

stack =[]
for _ in range(n):
    cmds = list(map(int,input().split()))

    cmd = cmds[0]
    if cmd==1:
        stack.append(cmds[1])
    elif cmd==2:
        try:
            print(stack.pop())
        except:
            print(-1)
    elif cmd==3:
        print(len(stack))
    elif cmd==4:
        if len(stack):
            print(0)
        else:
            print(1)
    elif cmd==5:
        try:
            print(stack[-1])
        except:
            print(-1)
    