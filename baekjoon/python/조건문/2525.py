hour, min = map(int, input().split())
time = int(input())

min += time

hour += min//60
min %=60
if hour>=24:
    hour-=24 

print(f'{hour} {min}')