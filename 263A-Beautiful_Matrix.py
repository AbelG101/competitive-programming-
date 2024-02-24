r1 = list(map(int, input().split()))
r2 = list(map(int, input().split()))
r3 = list(map(int, input().split()))
r4 = list(map(int, input().split()))
r5 = list(map(int, input().split()))

grid = [r1, r2, r3, r4, r5]

for r in range(5):
  for c in range(5):
    if grid[r][c] == 1:
      print(abs(2-r) + abs(2-c))
      break
