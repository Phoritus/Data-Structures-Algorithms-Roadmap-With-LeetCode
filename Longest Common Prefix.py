class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        minlen = float('inf')
        maxlen = float('-inf')
        for i in s:
            minlen = min(len(i),minlen)
            
        j=""

        i = 0
        while i < minlen:
            for j in s:
                if j[i] != s[0][i]:
                    return j[:i]
            i += 1
 

        return j[:i]