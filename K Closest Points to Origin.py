import heapq as hq

points = [[3, 3], [5, -1], [-2, 4]] ; k = 2

ans = []
for i in points:
    val = i[0]**2+i[1]**2
    if len(ans) < k:
        hq.heappush(ans, (-val,(i)))
    else:
        hq.heappushpop(ans, (-val,(i)))
print([n[1] for n in ans])

# Time: O(n log k) 
# Space: O(k)