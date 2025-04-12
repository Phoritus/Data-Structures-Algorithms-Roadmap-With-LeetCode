nums = [2,2,1,1,1,2,2]
ans = 0
c = 0
for i in nums:
    if c == 0:
        ans = i
    if i == ans:
        c += 1
    else:
        c -= 1
print(ans)
