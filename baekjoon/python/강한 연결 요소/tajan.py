# defaultdict
# dict이긴 한데 초기값을 지정할 수 있음

from collections import defaultdict

v,e = map(int, input().split())
graph = [[]for _ in range(v+1)]
for _ in range(e):
    a,b = map(int, input().split())
    graph[a].append(b)

# parent배열
d = [-1 for i in range(v+1)]

# 사이클이 됬을때 사이클 구성요소가 되는 스택
stack=[]
# 정점이 스택에 들어있나 확인
on_stack=[False for _ in range(v+1)]

def dfs(cur):
    print(stack)
    stack.append(cur)
    on_stack[cur]=True

    d[cur]=cur
    parent=d[cur]
    for next in graph[cur]:
        if d[next]==-1:
            parent = min(parent, dfs(next))
        elif on_stack[next]:
            parent = min(parent, d[next])
    
    # 갱신이 안됫으면 내가 사이클 대장
    if parent == d[cur]:
        scc=[]
        while True:
            node = stack.pop()
            on_stack[node]=False
            d[node]=parent
            scc.append(node)
            if cur==node:
                break
        print(scc)
    return parent

for i in range(1,v+1):
    if d[i]==-1:
        dfs(i)
print(d)