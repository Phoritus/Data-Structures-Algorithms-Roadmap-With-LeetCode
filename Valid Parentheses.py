s = "([])"
ham = {')':'(',']':'[','}':'{'}
stk = []
c = True
for i in s:
    if i not in ham:
        stk.append(i)
    else:
        if not stk:
            c = False
            break
        else:
            poped = stk.pop()
            if poped != ham[i]:
                c = False
                break
if not stk:
    print(c)
else:
    print(False)
# Time:O(n)
# Space:O(n)