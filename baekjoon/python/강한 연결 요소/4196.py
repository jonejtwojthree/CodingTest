import sys

input = sys.stdin.readline


def init():
    for _ in range(m):
        a,b=map(int, input().split())
        graph[a].append(b)

def scc(cur):
    global id, sccCount
    ret = parent[cur]=id
    id+=1

    stack.append(cur)
    on_stack[cur]=True

    for next in graph[cur]:
        if parent[next]==-1:
            ret = min(ret, scc(next))
        elif on_stack[next]==True:
            ret = min(ret, parent[next])
    
    if ret==parent[cur]:
        while True:
            tmp = stack.pop()
            on_stack[tmp]=False
            parent[tmp]=ret
            if tmp==ret:
                break
        sccCount+=1
    return ret

def solve():
    result=0

    for i in range(1,n+1):
        if parent[i]==-1:
            scc(i)
    print(parent)
   
    # 위상값 만드는 곳
    # 1->2->3->4면 [-1,0,1,2,3]이 되야해서 2중 for문
    for i in range(1, n+1):
        for next in graph[i]:
            if parent[next]==parent[i]:
                continue
            sccIndegree[parent[next]]+=1
    
    # print(sccIndegree)
    # print(sccCount)
    for i in range(1,sccCount+1):
        if sccIndegree[i]==0:
            result+=1
    
    print(result) 

t = int(input())
for _ in range(t):
    n,m=map(int, input().split())
    graph=[[] for _ in range(n+1)]
    stack=[]
    visited=[False]*(n+1)
    parent=[-1]*(n+1)
    on_stack=[False]*(n+1)
    sccIndegree=[0]*(n+1)
    
    id=1
    sccCount=0
    init()
    solve()