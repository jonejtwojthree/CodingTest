import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dy=[-2,-1,1,2,2,1,-1,-2]
dx=[-1,-2,-2,-1,1,2,2,1]


def my_bfs():
    l = int(input())
    cur_y, cur_x = map(int, input().split())
    end_y, end_x = map(int, input().split())

    visited = [[False for _ in range(l)] for _ in range(l)]    
    queue = deque([])
    queue.append((cur_y,cur_x,0))
    
    while queue:
        cur=queue.popleft()
        y=cur[0]
        x=cur[1]
        cnt=cur[2]

        if visited[y][x]==True:
            continue

        visited[y][x]=True
        
        if y==end_y and x==end_x:
            print(cnt)
            break

        for i in range(8):
            new_y=y+dy[i]
            new_x=x+dx[i]

            if 0<=new_y<l and 0<=new_x<l and visited[new_y][new_x]==False:
                queue.append((new_y, new_x, cnt+1))

def my_bfs_v2():
    l = int(input())
    cur_y, cur_x = map(int, input().split())
    end_y, end_x = map(int, input().split())

    visited = [[False for _ in range(l)] for _ in range(l)]    
    queue = deque([])
    queue.append((cur_y,cur_x,0))
    visited[cur_y][cur_x]=True

    while queue:
        cur=queue.popleft()
        y=cur[0]
        x=cur[1]
        cnt=cur[2]

        if y==end_y and x==end_x:
            print(cnt)
            break

        for i in range(8):
            new_y=y+dy[i]
            new_x=x+dx[i]

            if 0<=new_y<l and 0<=new_x<l and visited[new_y][new_x]==False:
                visited[new_y][new_x]=True
                queue.append((new_y, new_x, cnt+1))


def your_bfs():
    l = int(input())
    cur_y, cur_x = map(int, input().split())
    end_y, end_x = map(int, input().split())

    visited = [[0 for _ in range(l)] for _ in range(l)]    
    
    queue = deque([])
    queue.append((cur_y,cur_x))
    
    while queue:
        cur=queue.popleft()
        y=cur[0]
        x=cur[1]

        # if visited[y][x]==True:
        #     continue

        # visited[y][x]=True
        
        if y==end_y and x==end_x:
            print(visited[y][x])
            break

        for i in range(8):
            new_y=y+dy[i]
            new_x=x+dx[i]

            if 0<=new_y<l and 0<=new_x<l and visited[new_y][new_x]==0:
                visited[new_y][new_x]=visited[y][x]+1
                queue.append((new_y, new_x))

for _ in range(T):
    # my_bfs()
    my_bfs_v2()
    # your_bfs()