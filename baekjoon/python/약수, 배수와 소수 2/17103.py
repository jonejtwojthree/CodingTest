import sys

t = int(input())

max_n=1000000
arr = [True for i in range(int(max_n**0.5)+1)]

# max_n이하의 값들 중에 소수를 구하자
# 에라스토네츠의 수
# 최대값의 **0.5까지 구하면 됨
for i in range(2,int(max_n**0.5)):
    if arr[i]:
        for j in range(i+i, int(max_n**0.5)+1,i):
            arr[j]=False

for _ in range(t):
    result=0
    n = int(sys.stdin.readline().rstrip())

    # 두 수를 더하는 문제니까 //2 까지만 확인하면 됨
    for i in range(2,n//2+1):
        if arr[i] and arr[n-i]:
            result+=1
    print(result)
# for _ in range(t):
#     num = int(input())
