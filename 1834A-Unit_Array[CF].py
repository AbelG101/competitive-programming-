from collections import Counter

t = int(input())

for _ in range(t):
  n = int(input())
  a = list(map(int, input().split()))

  hm = {1: 0, -1: 0}

  for num in a:
    if num == 1:
      hm[1] += 1
    else: hm[-1] += 1

  operations = 0
  while((hm[-1] % 2 != 0 and hm[-1] != 0) or (hm[1] < hm[-1])):
    hm[-1] -= 1
    hm[1] += 1
    operations += 1

  print(operations)
