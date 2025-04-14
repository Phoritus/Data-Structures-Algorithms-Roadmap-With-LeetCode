numbers = [1,2,3,4,4,9,56,90]
target = 8
n = len(numbers)
i,j = 0,n-1
ans = []
while i < n:
    if numbers[i]+numbers[j] == target:
        ans.append(i+1)
        ans.append(j+1)
        break
    elif (numbers[i]+numbers[j])>target:
        j -= 1
    elif (numbers[i]+numbers[j])<target:
        i += 1
print(ans)