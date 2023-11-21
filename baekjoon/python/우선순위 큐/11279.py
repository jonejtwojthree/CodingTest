# Thread-Safe: Priority queue
# None -Thread-Safe: heapq

import sys, heapq


heap=[]
n=int(sys.stdin.readline())

for _ in range(n):
    num=int(sys.stdin.readline())

    if num==0:
        print(heapq.heappop(heap)*-1 if heap else 0)
    else:
        heapq.heappush(heap, -num)
