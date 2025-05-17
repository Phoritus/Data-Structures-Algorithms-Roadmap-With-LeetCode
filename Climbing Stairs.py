# In this code it contain 3 different methods to solve the Fibonacci Number problem
# 1. Use constant space
# 2. Use Top-Down Memoization
# 3. Use Bottom-Up Dynamic Programming


n = 5 # Test case 1, 2, 3, 4, 5
# n = 10 # Test case 2
prev, cur = 1,2
for i in range(2,n):
    prev, cur = cur, prev+cur
print(cur)
# Use constant space to adapt code
# Time complexity: O(n)
# Space complexity: O(1)

# dp = {1:1,2:2}
# def f(n):
#     if n == 1: return 1
#     if n == 2: return 2
#     if n in dp:
#         return dp[n]
#     else:
#         dp[n] = f(n-2) + f(n-1)
#         return dp[n]
# print(f(5))
# Use Top-Down Memoization 
# Time complexity: O(n)
# Space complexity: O(n)

# n = 5
# dp = [0] * n
# dp[0],dp[1] = 1,2
#
# for i in range(2,n):
#     dp[i] = dp[i-1] + dp[i-2]
#
# print(dp[-1])
# Use Bottom-Up Dynamic Programming
# Time complexity: O(n)
# Space complexity: O(n)
