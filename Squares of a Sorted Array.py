nums = [-4,-1,0,3,10]
result = []
i,j = 0,len(nums)-1
while i<=j:
    if abs(nums[i])>abs(nums[j]):
        result.append(pow(nums[i],2))
        i += 1
    else:
        result.append(pow(nums[j],2))
        j -= 1
result.reverse()
print(result)
