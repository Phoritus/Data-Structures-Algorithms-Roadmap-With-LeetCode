class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

a = TreeNode(20)
b = TreeNode(15)
c = TreeNode(25)
d = TreeNode(7)
e = TreeNode(17) ; f = TreeNode(24)

a.left = b ; a.right = c
b.left = d ; b.right = e
c.left = f
#        Tree
#         20
#        /  \
#      15    25
#     /  \   /
#    7   17 24
prev = [None]
md = [float('inf')]
def ser(root):
    if not root:
        return
    ser(root.left)
    if prev[0] is not None:
        md[0] = min(md[0],root.val-prev[0])
    prev[0] = root.val
    ser(root.right)

ser(a)
print(md[0])

# Instuitions:
# 1. We can use in-order traversal to get the elements in sorted order.
# 2. We can use a stack to do the in-order traversal iteratively.
# 3. We can keep track of the previous element and the minimum difference found so far.
# 4. We can update the minimum difference whenever we find a new element.
# 5. We can return the minimum difference at the end of the traversal.
# 6. We can also use a list to keep track of the previous element and the minimum difference.
# 7. We can use a list to keep track of the previous element and the minimum difference.
# 8. We can use a list to keep track of the previous element and the minimum difference.

#  Time Complexity: O(n)
#  Space Complexity: O(h) where h is the height of the tree.