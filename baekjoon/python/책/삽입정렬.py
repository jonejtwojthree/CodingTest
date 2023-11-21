# 삽입 정렬
# O(N^2)
# 정렬되있어야 됨

array=[3,4,5,1,2]

# # 첫 원소(idx:0)는 자체로 정렬되어 있음
# for i in range(1, len(array)):
#     find_idx=i

#     for j in range(i):
#         # j로 들어가고 j+1부터 밀림
#         if array[i] < array[j]:
#             find_idx=j
#             break
#     tmp=array[i]
#     for j in range(i,find_idx,-1):
#         array[j]=array[j-1]
#     array[find_idx] = tmp

# 첫 원소(idx:0)는 자체로 정렬되어 있음
for i in range(1, len(array)):
    for j in range(i,0,-1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]        
print(array)