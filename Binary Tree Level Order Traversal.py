class TreeNode():
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = left
        self.right = right


a = TreeNode(3)
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b ; a.right = c
c.left = d ; c.right = e
#       Tree
#         3
#        / \
#       9   20
#           /  \
#          15   7

from collections import deque # Using deque for efficient pop from the left side
# Level Order Traversal of a Binary Tree

def node(root):
    queue = deque() # Using deque for efficient pop from the left side
    queue.append(root)
    ans = []
    while queue:
        n = len(queue)
        level = []

        for i in range(n):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

        if level:
            ans.append(level)

    return ans

ans = node(a)
print(ans)
# [[3], [9, 20], [15, 7]]

# Time Complexity: O(n) where n is the number of nodes in the tree.
# Space Complexity: O(n) where n is the number of nodes in the tree.
# The space complexity is O(n) because we are using a queue to store the nodes at each level of the tree.