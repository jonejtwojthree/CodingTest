def matrix(A, B):
  global N
  lst = [[0 for i in range(N) ]for _ in range(N)]

  for i in range(N):
    for j in range(N):
      row_lst = A[i]
      col_lst = [ B[k][j] for k in range(len(B))]
      lst[i][j] =sum([aa*bb for aa, bb in zip(row_lst, col_lst)])%1000
  return lst

N, B = map(int, input().split())
A = []
for _ in range(N):
  A.append(list(map(int, input().split())))

tmp=A
for _ in range(B-1):
    tmp = matrix(A,tmp)

for row in tmp:
    print(*row)