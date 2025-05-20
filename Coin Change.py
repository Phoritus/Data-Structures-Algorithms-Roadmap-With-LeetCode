# In this code have 2 methods to solve the problem
# 1. Dynamic Programming Bottom Up
# 2. Dynamic Programming Top Down


# 1. Dynamic Programming Bottom Up
coins = [1,2,5] ; amount = 11
dp = [0] * (amount+1)
for i in range(1,amount+1):
    minn = float('inf')
    for coin in coins:
        diff = i - coin
        if diff < 0: break
        minn = min(minn, 1 + dp[diff])
    dp[i] = minn
print(dp[-1] if dp[-1] < float('inf') else -1 )
# Time Complexity: O(n*m) where n is the amount and m is the number of coins
# Space Complexity: O(n) where n is the amount


# 2. Dynamic Programming Top Down
# coins = [1,2,5] ; amount = 11
# memo = {0:0}
# def coin_count(amt):
#     if amt in memo:
#         return memo[amt]
#     minn = float('inf')
#     for coin in coins:
#         diff = amt - coin
#         if diff < 0: break
#         minn = min(minn,1 + coin_count(diff))
#         memo[amt] = minn
#     return minn
#
# result = coin_count(amount)
# if result < float('inf'):
#     print(result)
# else: print(-1)
# Time Complexity: O(n*m) where n is the amount and m is the number of coins
# Space Complexity: O(n) where n is the amount