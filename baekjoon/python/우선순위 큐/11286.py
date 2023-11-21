# Thread-Safe: Priority queue
# None -Thread-Safe: heapq
# heapq.heappush([], key)에서 key를 튜플로 지정하면  sort처럼 사용할 수 있음

import sys, heapq


heap=[]
n=int(sys.stdin.readline())

for _ in range(n):
    num=int(sys.stdin.readline())

    if num==0:
        print(heapq.heappop(heap)[1] if heap else 0)
    else:
        heapq.heappush(heap, (abs(num),num))
