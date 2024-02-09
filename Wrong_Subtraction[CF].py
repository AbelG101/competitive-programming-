num, counter = list(map(int, input().split()))

for _ in range(counter):
  if num % 10 == 0:
    num //= 10
  else:
    num -= 1

print(num)
