from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val} -> {self.next}"

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1
                head = list1
                list1 = list1.next
            else:
                head.next = list2
                head = list2
                list2 = list2.next
        head.next = list1 if list1 else list2
        return ans.next
        # Time: O(n)
        # Space: O(1)

# Helper functions for testing
def create_linked_list(vals):
    dummy = ListNode()
    current = dummy
    for val in vals:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(node):
    values = []
    while node:
        values.append(str(node.val))
        node = node.next
    print(" -> ".join(values))

if __name__ == '__main__':
    # Create two example sorted linked lists
    list1 = create_linked_list([1, 2, 4])
    list2 = create_linked_list([1, 3, 4])
    
    sol = Solution()
    merged = sol.mergeTwoLists(list1, list2)
    
    print("Merged list:")
    print_linked_list(merged)