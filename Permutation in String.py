s1 = "ab" ; s2 = "eidbaooo"
n1 = len(s1) ; n2 = len(s2)
count1 = [0]*26 ; count2 = [0]*26 ; c = False
for i in range(n1):
    count1[ord(s1[i])-ord('a')] += 1
    count2[ord(s2[i])-ord('a')] += 1
if count1 == count2:
    c = True
for i in range(n1,n2):
    count2[ord(s2[i])-ord('a')] += 1
    count2[ord(s2[i-n1])-ord('a')] -= 1
    if count1 == count2:
        c = True
        break
print(c)
# # Instuitions
# 1. We can use a sliding window approach to check if the second string contains a permutation of the first string.
# 2. We maintain two frequency arrays `count1` and `count2` to count the occurrences of each character in the first string and the current window of the second string, respectively.
# 3. We initialize the frequency arrays for the first window of the second string.
# 4. We then slide the window one character at a time, updating the frequency array for the second string by adding the new character and removing the character that is no longer in the window.
# 5. If the frequency arrays are equal at any point, it means the second string contains a permutation of the first string.
# 6. If no such window is found, we return False.
# # Time Complexity: O(n) or O(n2)
# # Space Complexity: O(1)