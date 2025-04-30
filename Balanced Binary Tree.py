class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.right = right
        self.left = left
    def __str__(self):
        return str(self.val)

a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)

a.left = b ; a.right = c
c.left = d ; c.right = e

balanced = [True] # Mutable object to store the balanced state
# This is a mutable object that can be modified inside the function without using the `nonlocal` or `global` keyword.

def height(root):

    if not root: # Base case: if the node is None, return height 0
        return 0

    left_height = height(root.left) # Recursively calculate the height of the left subtree
    if not balanced[0]: # If the tree is already unbalanced, no need to check further
        return 0
    right_height = height(root.right) # Recursively calculate the height of the right subtree

    if abs(left_height - right_height) > 1: # Check if the current node is balanced
        balanced[0] = False
        return 0

    return 1 + max(left_height,right_height) # Return the height of the current node

height(a) # Call the height function to start the recursion
print(balanced) # Print the balanced state of the tree

# Instuitions
# 1. We can use a recursive approach to check if the binary tree is balanced.
# 2. A binary tree is considered balanced if the height of the left and right subtrees of any node differ by at most 1.
# 3. We can define a helper function `height` that calculates the height of a subtree and checks if it is balanced at the same time.
# 4. We can use a mutable object (like a list) to keep track of the balanced state of the tree, so we can modify it inside the recursive function without using `nonlocal` or `global` keywords.
# 5. The base case for the recursion is when the node is None, in which case we return height 0.
# 6. We recursively calculate the height of the left and right subtrees and check if the current node is balanced.
# 7. If the current node is unbalanced, we set the balanced state to False and return 0.
# 8. Finally, we return the height of the current node as 1 plus the maximum height of its left and right subtrees.

# Time Complexity: O(n) - We visit each node once.
# Space Complexity: O(h) - The space complexity is O(h) due to the recursion stack, where h is the height of the tree.
