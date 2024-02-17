from math import gcd

n = int(input())
array = list(map(int, input().split()))

g = array[0]
for i in range(1, n):
    g = gcd(g, array[i])

if g == min(array):
    print(g)
else:
    print(-1)
