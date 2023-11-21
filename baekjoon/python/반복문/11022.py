# rstrip을 하라는 건 문자열 자체를 변수에 저장하고 싶을 때 얘기지, 개행문자가 맨 끝에 들어와도 int 변환이나 split()을 그대로 할 수 있습니다. 즉 int(sys.stdin.readline()), sys.stdin.readline().split() 이렇게 해도 아무 문제 없습니다. 
# 참고로 이름이 꽤 길기 때문에 저는 input = sys.stdin.readline을 맨 처음에 함으로써 쓰는 편입니다.

import sys

n = int(input())
lst = [ list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for i, nn in enumerate(lst):
    print(f'Case #{i+1}: {nn[0]} + {nn[1]} = {nn[0]+nn[1]}')