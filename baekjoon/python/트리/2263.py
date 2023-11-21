import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
# n = int(input())
# inorder = list(map(int, input().split()))
# postorder = list(map(int, input().split()))

n=11
inorder=[4,3,5,2,1,9,7,6,10,8,11]
postorder=[4,5,3,2,9,7,10,11,8,6,1]

results=[]
# lst: postorder
def f(inorder_start_idx, inorder_end_idx, postorder_start_idx, postorder_end_idx):
    if inorder_start_idx > inorder_end_idx or postorder_end_idx > postorder_end_idx:
        return
        
    num=postorder[postorder_end_idx-1]
    idx = inorder.index(num)
    results.append(num)
    print(num, idx)
    
    f(inorder_start_idx, idx, postorder_start_idx, idx)
    f(idx+1, inorder_end_idx, idx, postorder_end_idx-1)
f(0, len(inorder)-1, 0, len(postorder)-1)
print(results)