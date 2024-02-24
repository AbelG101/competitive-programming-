m, n = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(m)]


def check_matrix(A):
    for i in range(m):
        for j in range(n):
            # check if there exists a 1 in the corresponding row or column of A
            if B[i][j] == 0:
                if 1 in A[i] or 1 in [A[x][j] for x in range(m)]:
                    return False
            else:
                # check if all elements in the corresponding row or column of A are 0
                if not any(A[i]) and not any(A[x][j] for x in range(m)):
                    return False
    return True

A = [[1] * n for _ in range(m)]

# update matrix A based on the conditions to produce matrix B
for i in range(m):
    for j in range(n):
        if B[i][j] == 0:
            # set all the rows at the given col to 0
            for x in range(m):
                A[x][j] = 0
            # set all the cols at the given row to 0
            for y in range(n):
                A[i][y] = 0

if check_matrix(A):
    print("YES")
    for row in A:
        print(*row)
else:
    print("NO")
