import sys

while True:
    string = sys.stdin.readline().rstrip()
    
    # 최종 끝
    if string=='.':
        break
    
    stack=[]

    for ch in string:
        if ch == '[' or ch == '(':
            stack.append(ch)
        elif ch == ']' or ch == ')':
            try:
                if (ch == ']' and stack[-1]=='[') or  (ch ==')' and stack[-1]=='('):
                    stack.pop()
                else: # (있고 ]들어온 경우, [있고 )들어온 경우 -> 더 해보나마나 no
                    break
            except: # 아무것도 없는데 ], ) 들어온경우 -> 더 해보나마나 no
                stack.append(ch)
                break
    if len(stack) == 0:
        print('yes')
    else:
        print('no')
