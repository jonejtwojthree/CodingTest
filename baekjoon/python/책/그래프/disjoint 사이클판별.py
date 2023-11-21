# 최종 부모님 찾기
def find_parent(x):
    if parent[x]!=x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a,b):
    a=find_parent(a)
    b=find_parent(b)

    if a<b:
        parent[b]=a
    else:
        parent[a]=b

v,e = map(int, input().split())
#최초 나의 부모는 나
parent = [ i for i in range(v+1)]

cycle=False

for i in range(e):
    a,b = map(int, input().split())
    if find_parent(a) == find_parent(b):
        cycle=True
        break
    else:
        union_parent(a,b)

for i in range(1,v+1):
    print(find_parent(i), end=' ')
print()

