from collections import deque
n= int(input())

lst = [ i+1 for i in range(n)]
deq = deque(lst)

while len(deq)>1:
    deq.popleft()
    deq.append(deq.popleft())

print(deq[0])
