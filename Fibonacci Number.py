# Fibonacci Number
# Use memoization to optimize the Fibonacci function is Top
memo = {0:0,1:1}
def f(n):
    
    if n in memo:
        return memo[n]
    else:
        memo[n] = f(n-1) + f(n-2)
        return memo[n]

print(f(3))

# Time complexity: O(n)
# Space complexity: O(n)
