s = "AABACAAEAAAA" ; k = 0
l = 0 ; n = len(s) ; count = [0]*26
long = 0
for r in range(n):
    count[ord(s[r]) - ord('A')] += 1
    while (((r-l)+1)-max(count)) > k:
        count[ord(s[l]) - ord('A')] -= 1
        l += 1
    long = max(long,(r-l)+1)
print(long)
# Time: O(n) where n is the length of the string s.
# Space: O(1) for the count array of size 26.
# The code uses a sliding window approach to find the longest substring with at most k replacements.