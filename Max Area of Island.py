grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]

m, n = len(grid), len(grid[0])

def dfs(i,j):
    if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != 1:
        return 0
    else:
        grid[i][j] = 0
        return 1 + dfs(i,j+1) + dfs(i+1,j) + dfs(i,j-1) + dfs(i-1,j) # up, down, left, right
        # 4 directions

max_grid = 0

for i in range(m):
    for j in range(n):
        if grid[i][j] == 1:
            max_grid = max(max_grid, dfs(i,j))


print(max_grid)


# Time Complexity: O(m*n)
# Space Complexity: O(m*n)