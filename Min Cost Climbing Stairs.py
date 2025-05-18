# In this code use 3 dynamic programming methods
# 1. Bottom up approach
# 2. Top down approach
# 3. Space optimized approach

# Here we reduce the space complexity by only keeping track of the last two steps
cost = [10,15,20]
prev, cur = 0,0
n = len(cost)
for i in range(2,n+1):
    prev, cur = cur, min(prev+cost[n-2],cur+cost[n-1])

print(cur)
# Time complexity: O(n)
# Space complexity: O(1)


# Bottom up approach
# cost = [10,15,20]
# n = len(cost)
# dp = [0]*(n+1)
# for i in range(2,n+1):
#     dp[i] = min((dp[i-2]+cost[i-2]),(dp[i-1]+cost[i-1]))
#
# print(dp[-1])
# Time complexity: O(n)
# Space complexity: O(n)


# Top down approach
# cost = [10,15,20]
# n1 = len(cost)
# dp = {0:0,1:1}
# def recursive(n):
#     if n < 2: return 0
#
#     if n in dp:
#         return dp[n]
#     else:
#         dp[n] = min(recursive(n-1) + cost[n-1],recursive(n-2) + cost[n-2])
#         return dp[n]
#
# print(recursive(n1))
# Time complexity: O(n)
# Space complexity: O(n)