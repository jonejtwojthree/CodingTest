import sys

n = int(input())

sosu=int(n**0.5)
lst=[True]*(n+1)
lst[0]=lst[1]=False

for i in range(2,int(n**0.5)+1):
    if lst[i]==True:
        for j in range(2*i,n+1,i):
            lst[j]=False
    
arr = [ idx for idx, item in enumerate(lst) if item]

i=j=0 #모두 왼쪽에서 시작
total=arr[i]
cnt=0

# while j<len(arr)-1:
#     if total == n:
#         cnt+=1
#         total -=arr[i]
#         i+=1
#         j+=1
#         total +=arr[j]
#     elif total<n:
#         j+=1
#         total+=arr[j]
#     else:
#         total-=arr[i]
#         i+=1


while i<=j:
    if total > n:
        total -= arr[i]
        i+=1
    elif total == n:
        cnt+=1
        total -=arr[i]
        i+=1
    else:
        j+=1
        if j >= len(arr):
            break
        
        total +=arr[j]

print(cnt)