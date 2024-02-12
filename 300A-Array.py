n = int(input())
negatives, zeros, positives = [], [], []

for t in map(int, input().split()):
    if t < 0:
        negatives.append(t)
    elif t == 0:
        zeros.append(t)
    else:
        positives.append(t)

print(1, negatives[0])
if len(positives) == 0:
    print(2, negatives[1], negatives[2])
    del negatives[:3]
else:
    print(1, positives[0])
    del negatives[0]
    del positives[0]

print(len(negatives) + len(zeros) + len(positives), end=' ')
for val in negatives:
    print(val, end=' ')
for val in zeros:
    print(val, end=' ')
for val in positives:
    print(val, end=' ')
