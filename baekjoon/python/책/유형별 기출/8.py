import re
import sys
input = sys.stdin.readline

data = input().rstrip()

# # 알파벳을 대체함
# number = re.sub("[A-Z]",'',data)
# alpha = re.sub("[0-9]",'',data)

# alpha = (re.findall("[A-Z]",data))
# number = (re.findall("[0-9]",data))

# alpha.sort()
# number.sort()
# print(''.join(alpha)+''.join(number))

# print(re.search("[0-9]", data))

result=[]
value=0
for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()
if value != 0:
    result.append(str(value))

print(''.join(result))