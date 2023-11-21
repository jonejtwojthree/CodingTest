import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

arr=[]

# while True:
#     try:
#         x=int(input())
#         arr.append(x)
#     except:
#         break

for _ in range(9):
    x=int(input())
    arr.append(x)

# 인덱스 활용
def f(start, end):
    if start>end:
        return
    
    root= arr[start]
    
    idx=-1
    for i in range(start, end+1):
        if root < arr[i]:
            idx = i
            break
    
    if idx==-1:
        f(start+1,end)
    else:
        f(start+1, idx-1)
        f(idx,end)
    
    print(root)

# 배열을 나눠서 하기
def solution(A):
    # 받은 배열 길이가 0이면 return
    if len(A) == 0:
        return

    tempL, tempR = [], []
    # 첫번째 값을 루트 노드로 설정
    mid = A[0]
    # 나머지 배열에 대해 for문을 돌면서 루트보다 커지는 부분을 기록해서 L과 R로 나눈다.
    # for-else문
    for i in range(1, len(A)):
        if A[i] > mid:
            tempL = A[1:i]
            tempR = A[i:]
            break
    else:
    	#모두 mid보다 작은 경우
        # A가 1개밖에 없을때 A[1:] = []임
        tempL = A[1:]
    
    #왼쪽, 오른쪽 순으로 재귀 후 루트 노드 값 출력
    solution(tempL)
    solution(tempR)
    print(mid)

solution(arr)
# f(0,len(arr)-1)
