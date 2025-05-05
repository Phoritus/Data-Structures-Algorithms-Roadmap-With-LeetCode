class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right

a = TreeNode(10)
p = TreeNode(5)
c = TreeNode(20)
q = TreeNode(1)
d = TreeNode(7)
e = TreeNode(15)
f = TreeNode(25)
a.left = p ; a.right = c
p.left = q ; p.right = d
c.left = e ; c.right = f
#         Tree
#          10
#         /  \
#        5    20
#       / \   /  \
#      1   7  15  25

lca = [a] # Assign the root to lca[0]
# lca[0] will be used to store the lowest common ancestor of p and q.

def search(root,p,q):
    if not root:
        return

    lca[0] = root
    if root is p or root is q:
        return
    elif root.val < p.val and root.val < q.val:
        search(root.right,p,q)
    elif root.val > p.val and root.val > q.val:
        search(root.left,p,q)
    else:
        return

search(a,p,q)
print(lca[0]) # You can use lca[0].val to get the value of the lowest common ancestor.
# The code above defines a binary tree and finds the lowest common ancestor (LCA) of two nodes p and q.

# Instuitions: 
# 1. If the root is None, return None.
# 2. If the root is p or q, return the root.
# 3. If the root is less than both p and q, search in the right subtree.
# 4. If the root is greater than both p and q, search in the left subtree.
# 5. If the root is between p and q, return the root.
# 6. If the root is not between p and q, return the root.
# 7. If the root is between p and q, return the root.
# 8. If the root is not between p and q, return the root.

# Time complexity: O(h) where h is the height of the tree.
# Space complexity: O(h) where h is the height of the tree.
# The space complexity is O(h) because of the recursion stack.