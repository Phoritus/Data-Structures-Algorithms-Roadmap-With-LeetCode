from collections import Counter
nums = [1,1,1,2,2,2,2,3,3,3,3,3] ; k = 2
count = Counter(nums)
n = len(nums)
bucket = [0] * (n+1)
for num, freq in count.items():
    if bucket[freq] == 0:
        bucket[freq] = [num]
    else:
        bucket[freq].append(num)
print(bucket)
ans = []
for i in range(n,-1,-1): # Start from the largest frequency
    if bucket[i] != 0:
       ans.extend(bucket[i]) # Add the numbers with the current frequency to the answer list
    if len(ans) == k:
        break
print(ans) # Output: [2, 3]
# The code finds the kth largest element in an array using a bucket sort approach.

# Time Complexity: O(n)
# Space Complexity: O(n)
# The code uses a Counter to count the frequency of each number in the array.