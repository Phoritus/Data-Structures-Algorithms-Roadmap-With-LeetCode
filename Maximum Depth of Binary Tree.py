class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b  ;  a.right = c
c.left = d  ;  c.right = e


def pre_order(node):
    if not node:
        return 0
    right = pre_order(node.right)
    left = pre_order(node.left)

    return 1 + max(right,left)

print(pre_order(a))

# Instuitions
# 1. We can use a recursive approach to find the maximum depth of the binary tree.
# 2. The base case is when the node is None, in which case we return 0.
# 3. For each node, we recursively calculate the maximum depth of the left and right subtrees.
# 4. The maximum depth of the current node is 1 (for the current node) plus the maximum of the depths of the left and right subtrees.
# 5. We return the maximum depth of the binary tree.
# Time Complexity: O(n), where n is the number of nodes in the binary tree.
# Space Complexity: O(h), where h is the height of the binary tree (due to recursion stack).