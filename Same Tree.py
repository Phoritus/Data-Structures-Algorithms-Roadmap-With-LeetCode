class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
a.left = b ; a.right = c
# Tree
#    1
#   / \
#  2   3

a1 = TreeNode(1)
b1 = TreeNode(2)
c1 = TreeNode(3)
a1.left = b1 ; a1.right = c1
# Tree
#    1
#   / \
#  2   3

 

def check(root1,root2):
    if not root1 and not root2: # both are None
        return True

    if not root1 or not root2: # one of them is None
        return False

    if root1.val != root2.val: # values are not equal
        return False

    return check(root1.left,root2.left) and check(root1.right,root2.right) # check if the two trees are identical

print(check(a,a1))

# Instuitions
# 1. We can use a recursive approach to check if two binary trees are identical.
# 2. We check if both trees are None, in which case they are identical.
# 3. If one of the trees is None and the other is not, they are not identical.
# 4. If the values of the current nodes are not equal, the trees are not identical.
# 5. We recursively check the left and right subtrees of both trees.
# 6. If all checks pass, the trees are identical.
# 7. The function returns True if the trees are identical, otherwise it returns False.

# Time Complexity: O(n) or O(n + m) where n and m are the number of nodes in the two trees.
# Space Complexity: O(h) or O(h1 + h2) where h and h1 are the heights of the two trees.
