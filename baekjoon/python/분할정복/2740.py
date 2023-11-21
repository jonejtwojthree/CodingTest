def matrix(A, B):
  
  for i in range(N):
    for j in range(K):
      row_lst = A[i]
      col_lst = [ B[k][j] for k in range(len(B))]
      print(sum([aa*bb for aa, bb in zip(row_lst, col_lst)]), end=' ')
    print()
  
  
  return sum( [i*j for i,j in zip(row_lst, col_lst)] )

N, M = map(int, input().split())
A = []
for _ in range(N):
  A.append(list(map(int, input().split())))

M, K = map(int, input().split())
B = []
for _ in range(M):
  B.append(list(map(int, input().split())))

# N, K 행렬
matrix(A,B)