import sys

n = int(input())
cnt = 0
max_int = sys.maxsize
for num in range(666, max_int):
    if str(num).find("666") != -1:
        cnt += 1
        if n == cnt:
            print(num)
            break

# for num in range(666,1000000000):
#   if '666' in str(num):
#     cnt+=1

#   if cnt==n:
#     print(num)
#     break
