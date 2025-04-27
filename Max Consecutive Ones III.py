nums = [1,12,-5,-6,50,3] ; k = 4
l,r = 0,k-1
cur = 0
n = len(nums)
for i in range(k):
    cur += nums[i]
m_avg = cur/k
for i in range(k,n):
    cur += nums[i]
    cur -= nums[i-k]
    avg = cur/k
    m_avg = max(m_avg,avg)
print(m_avg)
# Intuition: We can use a sliding window of size k to find the maximum average subarray of size k.
# Time: O(n) where n is the length of nums.
# Space: O(1)
# Note: The code above is a simple implementation of the sliding window technique to find the maximum average subarray of size k.