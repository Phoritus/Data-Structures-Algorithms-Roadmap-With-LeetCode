import heapq as hq
from collections import defaultdict

# Dijkstra's Algorithm
# Given a list of times, where each time is a list of three integers [u, v, time],

times = [[2,1,1],[2,3,1],[3,4,1]] ; n = 4 ; k = 2
# Other test cases
# times = [[1,2,1],[2,3,2],[1,3,4]] ; n = 3 ; k = 1

graph = defaultdict(list)

for u, v, time in times:
    graph[u].append((v,time))


min_dis = {}
min_heap = [(0,k)]
seen = set()

while min_heap:
    k_to_n, i = hq.heappop(min_heap)
    if i in min_dis:
        continue

    min_dis[i] = k_to_n
    
    for nei, nei_dis in graph[i]:
        if nei not in min_dis:
            hq.heappush(min_heap,((k_to_n+nei_dis),nei))

print(max(min_dis.values()))

# Time complexity: O(ElogV), where E is the number of edges and V is the number of vertices.
# Space complexity: O(E+V), where E is the number of edges and V is the number of vertices.
# find the minimum time to reach all nodes from the starting node k.