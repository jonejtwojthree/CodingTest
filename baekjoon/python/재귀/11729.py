
def f(n, a, b, c): # 출발 경유 도착지
    global cnt, lst
    cnt+=1
    if n==1:
        lst.append((a, c))
        return
    f(n-1,a, c, b)          # n-1개 b 경유지로 옮김
    lst.append((a, c))      # n번째 c로 옮김
    f(n-1, b, a, c)         # n-1개 c로 옮김

n=int(input())
cnt=0
lst=[]
f(n,1, 2, 3)
print(cnt)
for ll in lst:
    print(ll[0], ll[1])