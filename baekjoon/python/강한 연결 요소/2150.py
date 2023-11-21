import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
v,e = map(int, input().split())
graph = [[] for _ in range(v+1)]

for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)

parent = [-1]*(v+1)
on_stack=[False]*(v+1)
stack=[]

scc=[]
# print(graph)

# id가 있어서 v가 1이든 v가5든 상관없이 id로 cycle집단을 대표할 수 있음
# stack에 아직 빠지지 않은 다른 사이클들도 있는데 그 노드들의 값을 v로 대체하면 min때문에 집단이 이상하게 만들어짐

id=0
def dfs(cur):
    global id
    # print(stack)
    stack.append(cur)
    id+=1
    parent[cur]=id
    on_stack[cur]=True

    p=parent[cur]
    for next in graph[cur]:
        if parent[next] == -1:
            p=min(p, dfs(next))
        elif on_stack[next]:
            p=min(p, parent[next])
    
    if parent[cur]==p:
        tmp=[]
        while True:
            node = stack.pop()
            on_stack[node]=False
            parent[node]=p
            tmp.append(node)
            if cur==node:
                break
        tmp.sort()
        tmp.append(-1)
        scc.append(tmp)
    return p

for i in range(1,v+1):
    if parent[i]==-1:
        dfs(i)

scc.sort()
print(len(scc))
for ll in scc:
    print(*ll)