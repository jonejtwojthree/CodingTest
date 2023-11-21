import sys
input = sys.stdin.readline

s = input().rstrip()
arr = [[0]*26]
arr[0][ord(s[0])-97] = 1

#알파벳 1개당 a~z까지 리스트 할당(값: 처음부터 idx까지 나온 a~z의 개수를 각각 넣어둠)
# arr[i][0]=k -> s문자열 i인덱스까지만 봤을때 'a'는  k개 들어있다.
for i in range(1,len(s)):
    arr.append(arr[-1][:])
    arr[i][ord(s[i])-97] += 1

#O(1)로 접근만 하면 됨
for _ in range(int(input())):
    c,start,end = list(input().split())
    start,end = map(int,[start,end])
    if start == 0:
        print(arr[end][ord(c)-97])
    else:
        print(arr[end][ord(c)-97]-arr[start-1][ord(c)-97])