matrix = [[1],[3]] ; target = 3 # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]] test case
m = len(matrix) ; n = len(matrix[0])
t = m * n
L = 0
R = t-1 # actually last integer in matrix
c = False
while L <= R:
    M = (L + R// 2)
    i, j = (M // n), (M % n)
    if matrix[i][j] == target:
        c = True
        print(matrix[i][j])
        break
    elif matrix[i][j] < target:
        L = M + 1
    else:
        R = M - 1
print(c)
# Time: O(log(m*n))
# Space: O(1)