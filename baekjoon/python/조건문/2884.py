hour, min = map(int, input().split())
if min < 45:
    if hour ==0:
        print(f'23 {min+15}')
    else:
        print(f'{hour-1} {min+15}')
else:
    print(f'{hour} {min-45}')