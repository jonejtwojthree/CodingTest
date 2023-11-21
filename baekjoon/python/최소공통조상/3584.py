import sys

input = sys.stdin.readline

t= int(input())
for _ in range(t):
    n=int(input())

    parent=[0 for i in range(n+1)]
    for _ in range(n-1):
        a,b = map(int, input().split())
        parent[b]=a
    # print(parent)
    
    v1,v2 = map(int, input().split())
    
    # 0을 넣은 이유는 v_parent 인덱스 에러 방지
    # 자신을 넣은 이유는 내가 남의 부모일 수 있어서(나를 넣지 않으면 내 위에가 최소 조상으로 잡힘)
    v1_parents, v2_parents = [0,v1], [0,v2]
    
    while parent[v1]:
        v1_parents.append(parent[v1])
        v1=parent[v1]
    
    while parent[v2]:
        v2_parents.append(parent[v2])
        v2=parent[v2]
    
    # print(v1_parents)
    # print(v2_parents)
    
    # 최상단부터 탐색(거꾸로 탐색)
    i=1
    while v1_parents[-i] == v2_parents[-i]:
        i+=1
    # print(v1_parents[-i+1])

    v1_idx=len(v1_parents)-1
    v2_idx=len(v2_parents)-1
    while v1_parents[v1_idx] == v2_parents[v2_idx]:
        v1_idx-=1
        v2_idx-=1
    print(v1_parents[v1_idx+1])    
    