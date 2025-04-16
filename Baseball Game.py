ops = ["5","-2","4","C","D","9","+","+"]
n = len(ops)
stk = []
for i in ops:
    if i == 'C':
        stk.pop()
    elif i == 'D':
        stk.append(stk[-1]*2)
    elif i == '+':
        stk.append(stk[-1]+stk[-2])
    else:
        stk.append(int(i))
print(stk)
print(sum(stk))
# Time:O(n)
# Space:O(n)
