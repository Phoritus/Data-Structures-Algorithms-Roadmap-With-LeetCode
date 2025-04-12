nums = [9,1,4,7,3,-1,0,5,8,-1,6]
s = set(nums)
c = 0
for i in nums:
    if i-1 not in s:
        next_num = i+1
        lent = 1

        while next_num in s:
            next_num += 1
            lent += 1
        c = max(c,lent)
print(c)
