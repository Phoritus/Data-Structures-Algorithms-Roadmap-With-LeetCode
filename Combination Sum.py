candidates = [2,3,6,7]  ; target = 7

def combinationSum(nums,target):
    n = len(nums)
    res, sol = [], []

    def backtrack(i, cur_sum):
        if cur_sum == target:
            res.append(sol[:])
            return

        if cur_sum > target or i == n:
            return

        backtrack(i+1,cur_sum) # skip the current number
        # include the current number

        sol.append(nums[i])
        backtrack(i, cur_sum+nums[i]) # fetch the same number again
        # backtrack
        sol.pop()
    backtrack(0,0)
    return res

print(combinationSum(candidates,target))

# Time Complexity: O(2^n)
# Space Complexity: O(n)
# The time complexity is O(2^n) because we are exploring all possible combinations of the input list.
# The space complexity is O(n) because we are using a list to store the current combination of numbers.