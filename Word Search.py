board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

def exist(board,word):
    m = len(board)
    n = len(board[0])
    w = len(word)

    def backtrack(pos, index):
        i, j = pos

        if w == index:
            return True

        if board[i][j] != word[index]:
            return False

        char = board[i][j]
        board[i][j] = '#'

        for i_off, j_off in [(0,1), (1,0), (-1,0), (0,-1)]: # right, down, up, left
            r, c = i + i_off, j + j_off # next cell
            if 0 <= r < m and 0 <= c < n: # check if in bounds
                if backtrack((r,c), index+1): # check if next cell is valid
                    return True

        board[i][j] = char # backtrack
        return False

    for i in range(m):
        for j in range(n):
            if backtrack((i,j), 0): # check if starting from this cell can lead to a solution
                return True

    return False

print(exist(board,word))

# Time Complexity: O((m*n)^2)
# Space Complexity: O(m*n)
# The time complexity is O((m*n)^2) because we are checking each cell in the board and for each cell, we are doing a DFS which can take O(m*n) time in the worst case.
# The space complexity is O(m*n) because we are using a stack to keep track of the cells we have visited and the maximum depth of the stack can be m*n in the worst case.
# The time complexity can be improved to O(m*n) by using a visited array to keep track of the cells we have visited instead of modifying the board.