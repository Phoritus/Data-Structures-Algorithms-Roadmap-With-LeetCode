class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left
    def __str__(self):
        return str(self.val)

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(5)
f = TreeNode(6)
g = TreeNode(7)
a.left = b ; a.right = c
b.left = d ; b.right = e
c.left = f ; c.right = g
# Tree structure:
#         1
#        / \
#       2   3 
#      / \ / \
#     4  5 6  7

d_long = [0] # Mutable to store the maximum diameter

def max_diameter(root):
    if not root:
        return 0 
    
    left = max_diameter(root.left)
    right = max_diameter(root.right)
    
    d = left + right # Diameter is the number of edges between two nodes
    # Update the maximum diameter found so far
    
    d_long[0] = max(d_long[0],d) # Store the maximum diameter in the mutable list
    return 1 + max(right,left)

max_diameter(a)
print(d_long[0])

# Instuitions
# 1. The diameter of a binary tree is the length of the longest path between any two nodes in the tree.
# 2. The path may or may not pass through the root.
# 3. The diameter is defined as the number of edges between the two nodes.
# 4. We can use a recursive approach to find the maximum diameter.
# 5. For each node, we calculate the maximum depth of its left and right subtrees.
# 6. The diameter at that node is the sum of the maximum depths of its left and right subtrees.
# 7. We keep track of the maximum diameter found so far.
# 8. The base case for the recursion is when the node is None, in which case we return 0.
# 9. The recursive case is to calculate the maximum depth of the left and right subtrees and update the maximum diameter.
# 10. Finally, we return the maximum depth of the current node, which is 1 plus the maximum of the left and right depths.

# Time Complexity: O(n) where n is the number of nodes in the tree
# Space Complexity: O(h) where h is the height of the tree (due to recursion stack)