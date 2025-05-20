nums = [2,3,1,1,4]
def canJump(nums):
    g = len(nums) - 1 # Initialize the goal to the last index
    for i in range(len(nums)-2,-1,-1): # Start from the second last index and go to the first index
        if nums[i] + i >= g:
            g = i
    return g == 0 # If you can reach the last index from the first index, goal will be 0

# Test the function
print(canJump(nums))  # Output: True

# Time Complexity: O(n) because we are iterating through the array once.
# Space Complexity: O(1) because we are using only a constant amount of space.