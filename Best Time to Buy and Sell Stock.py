class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1,w2 = len(word1),len(word2)
        in1,in2 = 0,0
        word = 1
        s = []
        while in1 < w1 and in2 < w2:
            if word == 1:
                s.append(word1[in1])
                in1 += 1
                word = 0
            else:
                s.append(word2[in2])
                in2 += 1
                word = 1

        while in1 < w1:
            s.append(word1[in1])
            in1 += 1

        while in2 < w2:
            s.append(word2[in2])
            in2 += 1
        
        return ''.join(s) # Merge the strings