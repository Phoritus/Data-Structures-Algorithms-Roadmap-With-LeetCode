class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(5)
b = TreeNode(4)
c = TreeNode(11)
d = TreeNode(7)
e = TreeNode(2)
f = TreeNode(8)
g = TreeNode(13)
h = TreeNode(4)
i = TreeNode(1)

a.left = b ; a.right = f
b.left = c
c.left = d ; c.right = e
f.left = g ; f.right = h
h.right = i
#        Tree
#         5
#       /   \
#      4     8
#     /     / \
#    11    13  4
#   /  \         \
#  7    2         1
target = 22
def find_sum(root,target,summ=0):
    if not root:
        return False # Base case: if the node is None, return False and check the next node.
    summ += root.val # Add the current node's value to the sum.

    if not root.left and not root.right and summ == target:
        return True 
 
    return find_sum(root.left,target,summ) or find_sum(root.right,target,summ)
    ## Recursive case: check the left and right subtrees.
    # If either subtree returns True, return True.
print(find_sum(a,target))

# Instuitions:
# 1. The function takes a binary tree and a target sum as input.
# 2. It uses recursion to traverse the tree and calculate the sum of the values from the root to the leaf nodes.
# 3. If the sum equals the target sum at a leaf node, it returns True.
# 4. If the sum does not equal the target sum, it continues to traverse the tree until all paths are checked.
# 5. If no path equals the target sum, it returns False.
# 6. The function uses a helper variable 'summ' to keep track of the current sum as it traverses the tree.
# 7. The function returns True if a path with the target sum is found, otherwise it returns False.
# 8. The function uses a depth-first search approach to explore all possible paths in the tree.
# 9. The function handles the case where the tree is empty by returning False immediately.
# 10. The function is designed to work with binary trees, where each node has at most two children.

# Time complexity: O(n) where n is the number of nodes in the tree.
# Space complexity: O(h) where h is the height of the tree, due to the recursion stack.
