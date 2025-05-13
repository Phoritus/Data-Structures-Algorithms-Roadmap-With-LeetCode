from collections import defaultdict
numCourses = 2 ; prerequisites = [[1,0],[0,1]]

d = defaultdict(list)
for u,v in prerequisites:
    d[u].append(v)


unvisited = 0
visiting = 1
visited = 2
state = [unvisited] * numCourses

def dfs(node):
    s = state[node]
    if s == visited: return True
    elif s == visiting: return False

    state[node] = visiting

    for nei in d[node]:
        if not dfs(nei): return False

    state[node] = visited # mark as visited
    return True

c = True

for i in range(numCourses):
    if not dfs(i):
        c = False

print(c)

# Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
# edage is a prerequisite of course j
# Space Complexity: O(V + E) for the graph representation
# Space Complexity: O(V) for the state array