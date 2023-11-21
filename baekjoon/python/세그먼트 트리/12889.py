import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


def init_min(start, end, index):
    if start==end:
        min_tree[index]=arr[start]
        return [min_tree[index]]
    mid = (start+end)//2
    min_tree[index]=init_min(start, mid, index*2) + init_min(mid+1, end, index*2+1)
    return min_tree[index]

# start, end는 segment트리가 만들어진 틀
# left, right가 내가 구하고 싶은 합의 구간
# left<=start<=end<=right 순이면 누적합을 구할 수 있는 구간임
def interval_min(start, end, index, left, right):
    if left > end or right < start: return INF
    if left <= start and right >= end:
        return min_tree[index]
    mid = (start+end)//2
    return (interval_min(start,mid, 2*index, left,right), interval_min(mid+1, end, 2*index+1, left,right))

n = map(int, input().split())
arr=[0]*(n+1)
INF=10**9

min_tree = [[]]*(n*4+1)

for  in range(n):
    a,b = map(int, input().split())
    
    if a==1:
        
    
init_min(1,n,1)
print(min_tree)
# # print(tree)
# for _ in range(m):
#     b,c = map(int, input().split())
#     print(interval_min(1,n,1,b,c), interval_max(1,n,1,b,c))