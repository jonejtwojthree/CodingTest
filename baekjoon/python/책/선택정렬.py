# 선택 정렬
# O(N^2)
# 정렬되있을 필요 없음

array=[3,4,5,1,2]

for i in range(len(array)):
    _min = array[i]
    _min_index = i

    for j in range(i+1, len(array)):
        if array[j] < _min:
            _min=array[j]
            _min_index=j
    array[i],array[_min_index] = array[_min_index],array[i]        
            
print(array)