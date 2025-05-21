nums = [10,9,2,5,3,7,101,18] ; n = len(nums)
dp = [1] * n
for i in range(n):
    j = 0
    while j < i:
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1) # Update dp[i] if we found a longer increasing subsequence
        j += 1

print(max(dp))

# Instuition
# 1. We are given a list of numbers and we need to find the length of the longest increasing subsequence.
# 2. We can use dynamic programming to solve this problem.
# 3. We create a dp array of the same length as the input list and initialize all values to 1.
# 4. We iterate through the input list and for each element, we check all previous elements to see if they are smaller.
# 5. If we find a smaller element, we update the dp array at the current index to be the maximum of its current value and the value at the previous index + 1.
# 6. Finally, we return the maximum value in the dp array as the length of the longest increasing subsequence.

# Time Complexity: O(n^2) because we have two nested loops.
# Space Complexity: O(n) because we are using a dp array of the same length as the input list.