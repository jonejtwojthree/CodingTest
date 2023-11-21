import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def init(start, end, index):
    if start==end:
        tree[index]=arr[start]
        return tree[index]
    mid = (start+end)//2
    tree[index] = init(start, mid, index*2) + init(mid+1, end, index*2+1)
    return tree[index]

# start, end는 segment트리가 만들어진 틀
# left, right가 내가 구하고 싶은 합의 구간
# left<=start<=end<=right 순이면 누적합을 구할 수 있는 구간임
def interval_sum(start, end, index, left, right):
    if left > end or right < start: return 0
    if left <= start and right >= end:
        return tree[index]
    mid = (start+end)//2
    return interval_sum(start,mid, 2*index, left,right) + interval_sum(mid+1, end, 2*index+1, left,right)

# index -> 구간합을 수정하고자 하는 노드
# node 현재 노드
def update(start, end, node, index, data):
    if index < start or index > end:
        return
    tree[node] += data
    
    if start==end:
        return

    mid = (start+end)//2
    update(start, mid, node*2, index, data)
    update(mid+1, end, node*2+1, index, data)


n = int(input())
tree = [0]*(n*4+1)

arr = [0] + list(map(int, input().split()))
    
init(1,n,1)

m = int(input())
# print(tree)
for _ in range(m):
    lst = list(map(int, input().split()))

    if lst[0]==1:
        num=lst[3]
        start, end=lst[1],lst[2]
        for i in range(start, end+1):
            update(1,n,1,i,num)
        # print(tree)
    elif lst[0]==2:
        print(interval_sum(1,n,1,lst[1],lst[1]))