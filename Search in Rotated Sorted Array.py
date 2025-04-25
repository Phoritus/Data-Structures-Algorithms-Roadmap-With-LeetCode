nums = [4,5,6,7,0,1,2] ; target = 1
n = len(nums) ; l = 0 ; r = n-1
while l<r:
    m = (l + (r-l)//2)
    if nums[m] > nums[r]:
        l = m + 1
    else:
        r = m
min_in = r
m = (0 + (len(nums)-0)//2)
c = -1
if nums[min_in] == nums[0]:
    l,r = 0,n-1
elif target >= nums[0] and target <= nums[m]:
    l,r = 0,min_in-1
else:
    l,r = min_in,n-1
while l<=r:
    m = (l + (r-l)//2)
    if nums[m] == target:
        c = m
        break
    elif nums[m] > target:
        r = m - 1
    else:
        l = m + 1
print(c)
# Time: O(2log(n)) or O(log(n))
# Space: O(1)
# # In intuition, we are trying to find the pivot point where the array is rotated.