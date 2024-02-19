n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

hm_a = {}
hm_c = {}

counter = 0

# create a hm for arr a & arr c
for i in range(len(a)):
    current = a[i]
    if current in hm_a:
        hm_a[current] += 1
    else:
        hm_a[current] = 1

for i in range(len(c)):
    current = c[i]
    if current in hm_c:
        hm_c[current] += 1
    else:
        hm_c[current] = 1

# iterate over arr b
for i in range(len(b)):
    # check if val exists in hm_a and current_idx + 1 exists in hm_c
    if b[i] in hm_a and i + 1 in hm_c:
        # increment counter by multiplying the counts
        counter += hm_a[b[i]] * hm_c[i + 1]

print(counter)
