class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self):
        return str(self.val)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(2)
d = TreeNode(3)
e = TreeNode(3)
f = TreeNode(4)
g = TreeNode(4)


a.left = b ; a.right = c
b.left = d ; b.right = g
c.left = g ; c.right = d
#     Tree
#         1
#        / \
#       2   2
#      / \ / \
#     3  4 4  3



def perfect(root1,root2):
    if not root1 and not root2: # if both are None
        return True
    if not root1 or not root2:
        return False
    if root1.val != root2.val:
        return False
    return perfect(root1.left,root2.right) and perfect(root1.right,root2.left) # check if left and right are same

print(perfect(a,a))
# Instuition:
# 1. If both trees are empty, they are the same.
# 2. If one tree is empty and the other is not, they are not the same.
# 3. If the values of the current nodes are not equal, they are not the same.
# 4. Recursively check the left subtree of the first tree with the right subtree of the second tree and vice versa.
# 5. If all the above conditions are satisfied, the trees are the same.

# Time Complexity: O(n)
# Space Complexity: O(h) where h is the height of the tree.