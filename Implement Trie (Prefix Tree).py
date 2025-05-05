class Trie:
    def __init__(self):
        self.Trie = {}

    def insert(self, word: str) -> None:
        d = self.Trie

        for s in word:
            if s not in d:
                d[s] = {}
            d = d[s]
        d['.'] = '.' # Mark the end of the word

    def search(self, word:str) -> bool:
        d = self.Trie

        for s in word:
            if s not in d:
                return False
            d = d[s]

        return '.' in d # Check if the end of the word is reached

    def prefix(self, word:str) -> bool:
        d = self.Trie

        for s in word:
            if s not in d:
                return False
            d = d[s]

        return True

obj = Trie()
obj.insert('apple')
c1 = obj.search('apple')
c2 = obj.search('app')
c3 = obj.prefix('app')
obj.insert('app')
c4 = obj.search('app')
ans = [c1,c2,c3,c4]
print(ans)

# Instuition:
# 1. Create a Trie class with an empty dictionary to store the Trie structure.
# 2. Implement the insert method to add words to the Trie.
# 3. Implement the search method to check if a word exists in the Trie.
# 4. Implement the prefix method to check if a prefix exists in the Trie.
# 5. Create an instance of the Trie class and test the methods with example words.
# 6. Print the results of the search and prefix methods to verify their functionality.
# 7. The output will show whether the words and prefixes were found in the Trie.
# 8. The Trie structure allows for efficient storage and retrieval of words and prefixes.
# 9. The search method returns True if the word exists, and False otherwise.
# 10. The prefix method returns True if the prefix exists, and False otherwise.
# 11. The insert method adds the word to the Trie, creating new nodes as needed.
# 12. The Trie structure is useful for applications such as autocomplete and spell checking.
# 13. The Trie can be used to efficiently store and search for a large number of words.
# 14. The Trie can also be used to find all words with a given prefix.
# 15. The Trie can be implemented using a nested dictionary structure, where each key represents a character.
# 16. The Trie can be implemented using a list of lists, where each index represents a character.
# 17. The Trie can be implemented using a class for each node, where each node has a dictionary of children.
# 18. The Trie can be implemented using a list of tuples, where each tuple represents a character and its children.
# 19. The Trie can be implemented using a list of strings, where each string represents a word.
# 20. The Trie can be implemented using a list of sets, where each set represents a character and its children.

# Time Complexity: O(n) for insert, search, and prefix methods, where n is the length of the word.
# Space Complexity: O(n) for the Trie structure, where n is the number of words inserted.
# The Trie structure allows for efficient storage and retrieval of words and prefixes.