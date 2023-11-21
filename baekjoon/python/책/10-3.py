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
        
v,e = map(int, input().split())
parent = [ i for i in range(v+1)]
edges=[]

for _ in range(e):
    a,b,cost = map(int, input().split())
    edges.append((cost,a,b))

edges.sort()
last=0
result=0

for edge in edges:
    cost,a,b=edge

    if find_parent(a) != find_parent(b):
        union_parent(a,b)
        result+=cost
        last=cost

print(result-last)
