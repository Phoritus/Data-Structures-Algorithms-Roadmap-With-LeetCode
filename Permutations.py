nums = [1,2,3]

def permute(num):
    n = len(num)
    res,sol = [], []
    def backtrack():
        if len(sol) == n:
            res.append(sol[:])

        for i in num:
            if i not in sol:
                sol.append(i)
                backtrack()
                sol.pop()
    backtrack()
    return res

print(permute(nums))
# Time complexity: O(n!)
# Space complexity: O(n)
# The time complexity is O(n!) because there are n! permutations of n elements.
# The space complexity is O(n) because we are using a list to store the current permutation.