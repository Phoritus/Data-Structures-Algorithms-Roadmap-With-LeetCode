class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        indmx = 0
        for i in range(len(nums)):
            if (abs(nums[i]) == abs(nums[indmx])):
                if(nums[i] > nums[indmx]):
                    indmx = i
            elif (abs(nums[i]) < abs(nums[indmx])):
                indmx = i
        return nums[indmx]
        