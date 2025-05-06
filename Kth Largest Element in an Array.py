import heapq as hq
nums = [3,2,1,5,6,4] ; k = 2

def check(arr):
    heap = []
    i = len(arr)
    for n in arr:
        if len(heap) < k:
            hq.heappush(heap, n)
        else:
            hq.heappushpop(heap, n)
    return heap[0]

print(check(nums))

# Instuitions:
# 1. We can use a min heap to keep track of the k largest elements in the array.
# 2. We can use the heapq module in Python to implement the min heap.
# 3. We can use the heappush and heappushpop functions to add elements to the heap and remove the smallest element.
# 4. We can use the len function to check the size of the heap and ensure that it does not exceed k.

# Time complexity: O(n log k) where n is the number of elements in the array and k is the size of the heap.
# Space complexity: O(k) where k is the size of the heap.
# The space complexity is O(k) because we are using a heap of size k to store the k largest elements.