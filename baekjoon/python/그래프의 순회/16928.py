import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int, input().split())

ladders=[]
snakes=[]

for _ in range(n):
    x,y = map(int, input().split())
    ladders.append((x,y))

for _ in range(m):
    u,v = map(int, input().split())
    snakes.append((u,v))

def bfs():
    queue=deque([])
    queue.append(1)
    graph=[0]*(101)

    while queue:
        cur = queue.popleft()

        if cur==100:
            print(graph[100])
            break
        for i in range(1,7):
            next=cur+i
            
            for ladder in ladders:
                if next == ladder[0]:
                    next=ladder[1]
                    break
            for snake in snakes:
                if next == snake[0]:
                    next=snake[1]
                    break
            
            if 0<=next<=100 and graph[next]==0:
                graph[next]=graph[cur]+1
                queue.append(next)
bfs()