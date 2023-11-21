
n = int(input())

numbers = list(map(int, input().split()))

snack_num = 1
stack = []

for number in numbers:
    # 넣고 보자
    stack.append(number)

    # 지금은 스택에서 snack_num을 빼야되는데 맨 위에 이게 있으면 ㅇㅋ
    while len(stack)>0 and snack_num == stack[-1]:
        stack.pop()
        snack_num+=1
    
if len(stack)==0:
    print('Nice')        
else:
    print('Sad')