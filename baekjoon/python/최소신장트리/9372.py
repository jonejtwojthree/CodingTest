import sys

input = sys.stdin.readline

t = int(input())
n,m = map(int, input().split())

for _ in range(t):
    edges = []
    
    for _ in range(m):
        a,b = map(int, input().split())
        # weight, start, dest
        edges.append((1,a,b))
        
    def kruskal():
        total_weight=0
        parent=[0]*(n+1)

        def find_parnet(x):
            if x != parent[x]:
                parent[x]=find_parnet(x)
            return parent[x]
        
        def union_parent(a,b):
            a=find_parnet(a)
            b=find_parnet(b)

            if a<b:
                parent[a]=b
            else:
                parent[b]=a
        
        for i in range()
    edges.sort()    
    kruskal()

