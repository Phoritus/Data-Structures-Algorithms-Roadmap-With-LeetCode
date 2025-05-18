# In this code use 3 methods to solve the problem of climbing stairs with minimum cost.
# 1. Dynamic Programming Bottom Up
# 2. Dynamic Programming with Space Optimization
# 3. Memoization


# Dynamic Programming with Space Optimization
nums = [2,7,9,3,1]
n = len(nums)
prev, cur = nums[0], max(nums[0],nums[1])
for i in range(2,n):
    prev, cur = cur, max(cur, prev+nums[i])
print(cur)
# Time complexity: O(n)
# Space complexity: O(1)


# Dynamic Programming Bottom Up
# nums = [2,7,9,3,1]
# if len(nums) == 1:
#      print(nums[0])
# n = len(nums)
# dp = [0]*n
# for i in range(n):
#     dp[i] = max(dp[i-1],dp[i-2]+nums[i])
# print(dp[-1])
# Time complexity: O(n)
# Space complexity: O(n)


# Memoization
# nums = [2,7,9,3,1]
# memo = {0:nums[0], 1:max(nums[0],nums[1])}
# def helper(n):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = max(helper(n-1),helper(n-2)+nums[n])
#         return memo[n]
#
# print(helper(len(nums)-1))
# Time complexity: O(n)
# Space complexity: O(n)