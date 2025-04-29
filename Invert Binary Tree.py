class TreeNode:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)
a = TreeNode(4)
b = TreeNode(2)
c = TreeNode(7) ; d = TreeNode(2) ; e = TreeNode(1) ; f = TreeNode(3)
g = TreeNode(6) ; h = TreeNode(9)

a.left = b ; a.right = c
b.left = e ; b.right = f
c.left = g ; c.right = h

def pre_order(node):
    if not node:
        return
    print(node)

    node.left, node.right = node.right, node.left
    pre_order(node.left)
    pre_order(node.right)


pre_order(a)
# Instuitions
# 1. We can use a recursive approach to invert the binary tree.
# 2. We start from the root node and swap its left and right children.
# 3. We then recursively call the function on the left and right children of the current node.
# 4. The base case for the recursion is when the node is None, in which case we simply return.
# 5. This approach effectively inverts the entire binary tree in a depth-first manner.
# Time Complexity: O(n), where n is the number of nodes in the tree.
# Space Complexity: O(h), where h is the height of the tree, due to the recursion stack.