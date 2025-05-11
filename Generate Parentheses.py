n = 3 # Another test case: n = 4, n = 5, n = 6, n = 7, n = 8, n = 9, n = 10
# This function generates all combinations of well-formed parentheses for a given number of pairs n.
# The function uses backtracking to explore all possible combinations of parentheses.

def generateParenthesis(n):
    res, sol = [], []

    def backtrack(openn, close):
        if len(sol) == 2*n: # It would be 2*n because we need n pairs of parentheses
            # When the length of the current combination is equal to 2*n,
            res.append(''.join(sol))
            return

        if openn < n:
            sol.append('(')
            backtrack(openn+1, close) 
            sol.pop()
        # This ensures that we never have more '(' than n and never have more ')' than n
             
        if openn > close:
            sol.append(')')
            backtrack(openn, close+1)
            sol.pop()
        # This ensures that we never have more ')' than '(' at any point 
        # because a valid parentheses string cannot have more closing parentheses than opening ones.
        
        
    backtrack(0,0)
    return res

print(generateParenthesis(n))

# Time Complexity: O(2**n)
# Space Complexity: O(n)
# The time complexity is O(2^n) because there are 2 choices at each level of the recursion tree (either add '(' or ')').
# The space complexity is O(n) because the maximum depth of the recursion tree is n, and we are using a list to store the current combination.
# The function generates all combinations of well-formed parentheses for a given number of pairs n.
