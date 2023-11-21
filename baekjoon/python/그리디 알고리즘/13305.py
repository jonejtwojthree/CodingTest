import sys

n, k = map(int,sys.stdin.readline().rstrip().split())

coins = []
for _ in range(n):
    num = int(sys.stdin.readline())
    coins.append(num)

coins.sort()


total=0
for i in range(len(coins)-1,-1,-1):
    coin=coins[i]
    total += k//coin
    k%=coin
print(total)