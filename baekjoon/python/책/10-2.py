def find_parent(x):
    if parent[x]!=x:
        parent[x]=find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a = find_parent(a)
    b = find_parent(b)
    
    if a<b:
        parent[b]=a
    else:
        parent[a]=b
        
n,m = map(int, input().split())
parent = [ i for i in range(n+1)]

for i in range(m):
    oper,a,b = map(int, input().split())

    if oper == 0:
        union_parent(a,b)
    elif oper==1:
        if find_parent(a) == find_parent(b):
            print("YES")
        else:
            print("NO")
            