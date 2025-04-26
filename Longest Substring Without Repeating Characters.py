s = "abcabcbb"
temp = set()
l,r = 0,0
long = 0
for r in range(len(s)):
    if s[r] in temp:
        temp.remove(s[l])
        l += 1
    w = (r-l)+1
    temp.add(s[r])
    long = max(long,w)
print(long)

# Instuitions:
# 1. Use a set to track characters in the current substring.
# 2. Use two pointers to define the current substring's bounds.
# 3. If a character is repeated, move the left pointer to the right until the substring is valid again.
# 4. Update the maximum length of the substring found so far.
# 5. Continue until the right pointer has traversed the entire string.
# 6. Return the maximum length found.
# Time: O(n) where n is the length of the string s.
# Space: O(1) since the set can only contain at most 26 characters (assuming only lowercase letters).