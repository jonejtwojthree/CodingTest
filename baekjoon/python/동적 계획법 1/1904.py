import sys
n=int(input())

if n==1 or n==2:
    print(n)
    sys.exit(1)

a=1
b=2
result=0

# 연산 할때마다 나누어줘야 시간에 안걸림
for i in range(3,n+1):
    result=(a+b)%15746
    a=b%15746
    b=result%15746

print(result)