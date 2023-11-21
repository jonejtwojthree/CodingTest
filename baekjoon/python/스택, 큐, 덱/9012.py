import sys

n = int(sys.stdin.readline())
for _ in range(n):
    vpss = sys.stdin.readline().rstrip()
    stack = []
    
    for vps in vpss:
        if vps=='(':
            stack.append(vps)
        else:
            try:
                stack.pop()
            except:
                # len>0을 유도하려고
                stack.append(vps)
                break
            
    if len(stack)==0:
        print("YES")
    else:
        print("NO")