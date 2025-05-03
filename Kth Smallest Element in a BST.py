class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    index = 1

    while index < len(values):
        node = queue.pop(0)

        if values[index] is not None:
            node.left = TreeNode(values[index])
            queue.append(node.left)
        index += 1

        if index < len(values) and values[index] is not None:
            node.right = TreeNode(values[index])
            queue.append(node.right)
        index += 1

    return root


values = [5, 3, 6, 2, 4, None, None, 1]
root = build_tree(values)
#       Tree
#         5
#        / \
#       3   6
#      / \
#     2   4
#    /
#   1

k = 3

def inorder(root,k):
    c = 0
    stk = []
    cur = root
    while cur or stk:
        while cur:
            stk.append(cur)
            cur = cur.left
        cur = stk.pop()
        c += 1
        if c == k:
            return cur.val
        cur = cur.right

print(inorder(root,k))