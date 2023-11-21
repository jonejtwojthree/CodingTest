import heapq

n = int(input())
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

result = 0

while len(heap) != 1:
    one = heapq.heappush(heap)
    two = heapq.heappush(heap)
    
    _sum = one+two
    result += _sum
    heapq.heappush(heap, _sum) 
print(result)