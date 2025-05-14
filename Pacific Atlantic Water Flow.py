from collections import deque
heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
hei = heights

p_que = deque()
p_seen = set()
# the Pacific Ocean

a_que = deque()
a_seen = set()
# the Atlantic Ocean

m, n = len(hei), len(hei[0])

for j in range(n):
    p_que.append((0,j))
    p_seen.add((0,j))
# look at the first row and add all the cells to the queue and seen set

for i in range(1,m):
    p_que.append((i,0))
    p_seen.add((i,0))
# look at the first column and add all the cells to the queue and seen set

for i in range(m):
    a_que.append((i,n-1))
    a_seen.add((i,n-1))
# look at the last column and add all the cells to the queue and seen set

for j in range(n-1):
    a_que.append((m-1,j))
    a_seen.add((m-1,j))
# look at the last row and add all the cells to the queue and seen set


def bfs(que, seen):
    while que:
        i, j = que.popleft()
        for i_offset, j_offset in ([0,1],[1,0],[-1,0],[0,-1]):
            # ([0,1] is right, [1,0] is down, [-1,0] is up, [0,-1] is left)
            
            r, c = i + i_offset, j + j_offset # check the neighbors
            
            if 0 <= r < m and 0 <= c < n and hei[r][c] >= hei[i][j] and (r,c) not in seen:
            # check if the cell is in bounds, if the height is greater than or equal to the current cell, and if we have not seen it before
                seen.add((r,c)) # add to the seen set because we are visiting it
                
                que.append((r,c)) # add to the queue because we need to check its neighbors

    return seen

p_ocean = bfs(p_que, p_seen)
a_ocean = bfs(a_que, a_seen)
print(p_ocean.intersection(a_ocean)) # Use intersection to find the cells that are reachable from both oceans

# Time complexity: O(m*n) because we are visiting each cell at most once
# Space complexity: O(m*n) because we are storing the cells in the queue and the seen set