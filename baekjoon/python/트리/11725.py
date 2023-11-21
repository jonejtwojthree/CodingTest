# import sys
# input = sys.stdin.readline

# # 정점 개수
# n = int(input())

# # zero index dummy 
# trees = [-1 for i in range(n+1)]

# # trees[k] = a  k의 부모는 a
# # 자기자신이 부모
# trees[1]=1


# for _ in range(n-1):
#     a,b = map(int, input().split())
    
#     # -1이 아니면 a의 부모는 이미 정해져 있음
#     if trees[a] != -1:
#         trees[b]=a
#     else:
#         trees[a]=b

# for item in trees[2:]:
#     print(item)

import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# 정점 개수
n = int(input())

# zero index dummy 
trees = [[] for i in range(n+1)]
parents = [-1 for i in range(n+1)]
parents[1]=1

for _ in range(n-1):
    a,b = map(int, input().split())
    trees[a].append(b)
    trees[b].append(a)

def bfs(i):
    queue = deque([])
    queue.append(i)

    while queue:
        cur = queue.popleft()

        for next in trees[cur]:
            if parents[next] ==-1:
                parents[next]=cur
                queue.append(next)

def dfs(cur):
    for next in trees[cur]:
        if parents[next]==-1:
            parents[next]=cur
            dfs(next)


def dfs_v2(i):
    # dfs stack버전은 reverse를 해야됨
    for tree in trees:
        tree.sort(reverse=True)

    stack=[i]
    while stack:
        cur=stack.pop()
        for next in trees[cur]:
            if parents[next]==-1:
                parents[next]=cur
                stack.append(next)

# dfs(1)
dfs_v2(1)
# bfs(1)

print(*parents[2:])