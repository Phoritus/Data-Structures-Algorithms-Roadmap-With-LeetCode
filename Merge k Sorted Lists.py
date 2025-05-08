import heapq as hq
class ListNode: # Definition for singly-linked list.
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def print_linked_list(arr): # Function to print the linked list
    cur = arr
    while cur:
        print(cur.val,end='->')
        cur = cur.next
    print(None)


lists = [[1,4,5],[1,3,4],[2,6]] # Example input
linked_list = [] # Convert the list of lists to a list of linked lists

for item in lists: 
    d = ListNode()
    cur = d
    for i in item:
        cur.next = ListNode(i)
        cur = cur.next
    linked_list.append(d.next) 
# linked_list is now a list of linked lists
# Example: linked_list = [1->4->5, 1->3->4, 2->6]

def mergeKLists(lists): # Function to merge k sorted linked lists
    heap = []

    for i, node in enumerate(lists):
        if node:
            hq.heappush(heap, (node.val, i, node))

    d = ListNode()
    cur = d
    while heap:
        val, i, node = hq.heappop(heap)
        cur.next = node
        cur = node
        node = node.next
        if node:
            hq.heappush(heap, (node.val, i, node))
    return d.next

merge = mergeKLists(linked_list)
print_linked_list(merge)

# Time: O(n log k)
# Space: O(k) k is the number of lists
# The time complexity is O(n log k) because we are pushing and popping from the heap k times for each of the n elements in the lists.