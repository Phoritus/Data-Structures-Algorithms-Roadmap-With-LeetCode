height = [0,1,0,2,1,0,1,3,2,1,2,1]
l_w,r_w = 0,0
n = len(height)
l_arr,r_arr = [0]*n,[0]*n
for i in range(n):
    j = -i-1
    l_arr[i] = l_w
    r_arr[j] = r_w
    l_w = max(height[i],l_arr[i])
    r_w = max(height[j],r_arr[j])
summ = 0
print(l_arr,r_arr)
for i in range(n):
    pot = min(l_arr[i],r_arr[i])
    summ += max(0,pot-height[i])
print(summ)