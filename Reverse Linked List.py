class SinglyNode:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next

values = [1,1,2]
temp = SinglyNode(0)
curr = temp
for val in values:
    curr.next = SinglyNode(val)
    curr = curr.next
head = temp.next

cur = head
while cur and cur.next:
    if cur.val == cur.next.val:
        cur.next = cur.next.next
    else:
        cur = cur.next

result = []
while head:
    result.append(head.val)
    head = head.next
print(result)

# Time: O(n)
# Space: O(1)