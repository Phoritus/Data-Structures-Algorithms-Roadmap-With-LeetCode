class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

# Main root
a = TreeNode(3)
b = TreeNode(4)
c = TreeNode(5)
d = TreeNode(1)
e = TreeNode(2)

a.left = b ; a.right = c
b.left = d ; b.right = e
#      Tree
#       3
#      / \
#     4   5
#    / \
#   1   2


# Sub root:
a1 = TreeNode(4)
b1 = TreeNode(1)
c1 = TreeNode(2)

a1.left = b1 ; a1.right = c1
#    Tree
#     4
#    / \
#   1   2


def equal(p,q): # check if two trees are equal
    if not p and not q:
        return True
    if not p or not q:
        return False
    if p.val != q.val:
        return False

    return equal(p.left,q.left) and equal(p.right,q.right)

def has_node(root,subtree): # check if the subtree is in the main tree
    if not root:
        return False
    if equal(root,subtree):
        return True

    return has_node(root.left,subtree) or has_node(root.right,subtree)

print(has_node(a,a1))

# Instuition:
# 1. Check if the root is None, if it is, return False.
# 2. Check if the root is equal to the subtree, if it is, return True.
# 3. Recursively check the left and right children of the root to see if they contain the subtree.
# 4. If the subtree is found in either the left or right child, return True.
# 5. If the subtree is not found in either child, return False.
# 6. The function uses a helper function equal to check if two trees are equal.
# 7. The equal function checks if both trees are None, if one is None, or if the values of the nodes are not equal.
# 8. If all checks pass, it recursively checks the left and right children of both trees to see if they are equal.
# 9. The function returns True if the trees are equal, and False otherwise.

# Time complexity: O(n*m) where n is the number of nodes in the main tree and m is the number of nodes in the subtree.
# Space complexity: O(h) or O(h + n) where h is the height of the main tree and n is the number of nodes in the subtree.
# The space complexity is due to the recursion stack used in the function calls.
