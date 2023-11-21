# arr을 -기준으로 split을 하면
# (1+2+3) - (1+2+3) - (1+2+3) 이렇게 됨
# arr[0]을 모두 더하고 이후에 값들은 모두 빼버리면됨
arr =  input().split('-')
s=0
for i in arr[0].split('+'):
    s += int(i)
for i in arr[1:]:
    for j in i.split("+"):
        s -= int(j)
print(s)