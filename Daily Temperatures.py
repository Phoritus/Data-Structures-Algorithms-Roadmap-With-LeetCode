temperatures = [73,74,75,71,69,72,76,73]
stk = []
ans = [0]*len(temperatures)
for i,v in enumerate(temperatures):
    while stk and v > temperatures[stk[-1]]:
        stk_i = stk.pop()
        ans[stk_i] = i-stk_i
    stk.append(i)
print(ans)
# Time: O(n)
# Space: O(n)