class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

adjList = [[2,4],[1,3],[2,4],[1,3]]
o_to_n = {}
def cloneGraph(node):
    start = node
    stk = [start]  # stack to keep track of nodes to visit
    visited = set()
    visited.add(start) # mark the start node as visited

    while stk:
        node = stk.pop() # pop the last node from the stack
        
        o_to_n[node] = Node(val=node.val) # create a new node for the old node
        
        for nei in node.neighbors:
            if nei not in visited:
                visited.add(nei)
                stk.append(nei)

    for old_node, new_node in o_to_n.items():
        for nei in old_node.neighbors:
            new_nei = o_to_n[nei] # get the new node
            # In o_to_n, the old node is the key and the new node is the value
            
            new_node.neighbors.append(new_nei) # add the new node to the neighbors of the new node
    # return the new node corresponding to the start node

    return o_to_n[start]

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.neighbors = [node2, node4]
node2.neighbors = [node1, node3]
node3.neighbors = [node2, node4]
node4.neighbors = [node1, node3]

cloned_graph = cloneGraph(node1)

result = []
for node in [node1, node2, node3, node4]:
    result.append([neighbor.val for neighbor in o_to_n[node].neighbors])

print(result)