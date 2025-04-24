nums = [4,5,6,7,0,1,2]
n = len(nums)
l = 0 ; r = n-1
while l<r:
    m = (l + (r-l)//2)
    if nums[m] > nums[r]:
        l = m + 1 # Move to the right half
    else:
        r = m # Move to the left half
print(nums[r])
# Time: O(log(n))
# Space: O(1)
# In intuition, we are trying to find the pivot point where the array is rotated.
