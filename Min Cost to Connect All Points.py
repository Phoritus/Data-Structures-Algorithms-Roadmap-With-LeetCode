import heapq as hq

# Prim's Algorithm
# Given a list of points, find the minimum distance to connect all points 

points = [[0,0],[2,2],[3,10],[5,2],[7,0]]

seen = set()
min_heap = [(0,0)]
n = len(points)
total_dis = 0

while len(seen) < n:
    dis, i = hq.heappop(min_heap)
    if i in seen:
        continue
    seen.add(i)
    xi, yi = points[i]
    total_dis += dis
    for j in range(n):
        if j not in seen:
            xj, yj = points[j]
            distance = abs(xi-xj) + abs(yi-yj)
            hq.heappush(min_heap,(distance,j))


print(total_dis)

# Time: (n^2 log(n))
# Space: (n^2)
