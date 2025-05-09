n = 4 ; k = 2
def combine(n, k):
    res, sol = [], []

    def backtrack(i):
        if len(sol) == k:
            res.append(sol[:])
            return

        left = i
        need = k - len(sol)
        if left > need: # pruning
            backtrack(i-1)
        sol.append(i)
        backtrack(i-1)
        sol.pop()

    backtrack(n)
    return res

print(combine(n,k))

# Time complexity: O(n!/(n-k)!) or O(n choose k)
# Space complexity: O(k)
# The time complexity is O(n!/(n-k)!) because we are generating all combinations of n choose k.
# The space complexity is O(k) because we are using a list to store the current combination of size k.