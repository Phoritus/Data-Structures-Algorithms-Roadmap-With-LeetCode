from collections import deque

grid = [[2,1,1],[1,1,0],[0,1,1]]

def orangesRotting(grid):
    q = deque()
    fresh, rotten = 1, 2
    num_fresh = 0
    time = -1
    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == rotten:
                q.append((i,j))
            elif grid[i][j] == fresh:
                num_fresh += 1

    if num_fresh == 0:
        return 0


    while q:
        q_size = len(q)
        time += 1
        for _ in range(q_size):
            i, j = q.popleft()

            for r, c in ([i,j+1], [i+1,j], [i,j-1], [i-1,j]):
                if 0 <= r < m and 0 <= c < n and grid[r][c] == fresh:
                    grid[r][c] = rotten
                    num_fresh -= 1
                    q.append((r, c))

    if num_fresh == 0:
        return time
    else:
        return -1


print(orangesRotting(grid))

# Time Complexity: O(m*n)
# Space Complexity: O(m*n)