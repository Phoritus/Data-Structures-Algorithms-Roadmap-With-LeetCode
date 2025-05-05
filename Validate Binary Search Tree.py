class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

a = TreeNode(5)
b = TreeNode(1)
c = TreeNode(4)
d = TreeNode(3)
e = TreeNode(6)
a.left = b ; a.right = c
c.left = d ; c.right = e
#      Tree
#        5
#       / \
#      1   4
#         / \
#        3   6
#   The tree is not a valid BST because 3 is less than 4 but is in the right subtree of 4.


def  valid(root,minn,maxx):
    if not root:
        return True

    if root.val >= maxx or root.val <= minn:
        return False

    return valid(root.left,minn,root.val) and valid(root.right,root.val,maxx)

print(valid(a,float('-inf'),float('inf')))

# Instuitions:
# 1. A binary search tree (BST) is a binary tree in which every node follows the below properties:
#    - The left subtree of a node contains only nodes with keys less than the node's key.
#    - The right subtree of a node contains only nodes with keys greater than the node's key.
#    - Both the left and right subtrees must also be binary search trees.
# 2. The function `valid` checks if a binary tree is a valid BST by recursively checking the value of each node against the allowed range defined by `minn` and `maxx`.
# 3. The base case for the recursion is when the node is `None`, in which case it returns `True` (an empty tree is a valid BST).
# 4. If the current node's value is not within the allowed range, it returns `False` (the tree is not a valid BST).
# 5. The function then recursively checks the left and right subtrees, updating the allowed range for each subtree.
# 6. The left subtree's maximum value is the current node's value, and the right subtree's minimum value is the current node's value.
# 7. The function returns `True` if both subtrees are valid BSTs, and `False` otherwise.
# 8. The initial call to the function starts with the entire range of possible values for a BST, which is negative infinity to positive infinity.
# 9. The final result indicates whether the entire tree is a valid BST or not.

# Time Complexity: O(n), where n is the number of nodes in the tree. Each node is visited once.
# Space Complexity: O(h), where h is the height of the tree. This is due to the recursion stack. In the worst case (unbalanced tree), h can be n, leading to O(n) space complexity. In a balanced tree, h is log(n), leading to O(log(n)) space complexity. 