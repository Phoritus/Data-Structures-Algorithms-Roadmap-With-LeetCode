from collections import defaultdict
strs = ["eat","tea","tan","ate","nat","bat"]
ans = defaultdict(list)
new = []
for i in strs:
    count = [0]*26
    for c in i:
        count[ord(c)-ord('a')] += 1

    key = tuple(count)
    ans[key].append(i)

print(list(ans.values()))