from collections import defaultdict
numCourses = 4 ; prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# False case
# numCourses = 2 ; prerequisites = [[1,0],[0,1]]

d = defaultdict(list)
course = prerequisites

for u,v in course:
    d[u].append(v)

unvisited = 0
visiting = 1
visited = 2

state = [unvisited] * numCourses
ans = []

def dfs(node):
    s = state[node]
    if s == visited:
        return True
    elif s == visiting:
        return False
    state[node] = visiting
    for nei in d[node]:
        if not dfs(nei):
            return False

    state[node] = visited
    ans.append(node)
    return True


for i in range(numCourses):
    if not dfs(i):
        ans = []
        break

print(ans)

# Time Complexity: O(V + E) because we visit each node and edge once
# where V is the number of vertices (courses) and E is the number of edges (prerequisites).


# Space Complexity: O(V + E) be
# because we use a dictionary to store the graph and a list to store the state of each node.
# The space complexity is dominated by the space used to store the graph and the state list.