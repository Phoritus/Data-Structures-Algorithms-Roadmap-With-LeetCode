height = [1,8,6,2,5,4,8,3,7]
n = len(height)-1
l,h = 0,n
length = n
max1 = 0
while l<h:
    if  min(height[l],height[h])*length > max1:
        max1 = min(height[l],height[h])*length
    if height[l]<height[h]:
        l += 1
        length -= 1
    elif height[l]>height[h]:
        h -=1
        length -= 1
    elif height[l]==height[h]:
        l += 1
        length -= 1
print(max1)
