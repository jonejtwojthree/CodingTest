n = int(input())

length=list(map(int, input().split()))
money = list(map(int, input().split()))

cur_idx=0
total=0
while cur_idx<len(length):
    next_idx=cur_idx
    for i in range(cur_idx+1,len(money)):
        if money[i] < money[cur_idx]:
            total += money[cur_idx]*sum(length[cur_idx:i])
            next_idx=i
            break
    
    if cur_idx == next_idx:
        total += money[cur_idx]*sum(length[cur_idx:])
        break
    else:
        cur_idx = next_idx
    print(f" cur_idx: {cur_idx}, total: {total}")
    # input()

# total += money[cur_idx]*sum(length[cur_idx:len(money)])

print(total)


N = int(input())
km = list(map(int, input().split()))
oil = list(map(int,input().split()))

cur_k = km[0]
cur_oil = oil[0]
s = cur_oil*km[0]
cur=1

while cur < len(km):
  if cur_oil > oil[cur]:
    cur_oil = oil[cur]
  s += cur_oil*km[cur]
  cur+=1
  
print(s)
  