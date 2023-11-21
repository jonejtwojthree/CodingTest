from collections import deque

graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

visited = [False]*9

def dfs(x):
    
    if visited[x]==True:
        return 
    
    print(x)
    visited[x]=True


    for i in graph[x]:
        if visited[i] == False:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited[start]=True
    while queue:
        cur = queue.popleft()
        print(cur)
        for i in graph[cur]:
            if visited[i] == False:
                visited[i]=True
                queue.append(i)
                
# print(dfs(1))
print(bfs(1))
