digits = "23" # Other test case "234", "2345", "23456", "234567", "2345678", "23456789"
# This code generates all possible letter combinations that the number could represent.

def letterCombinations(digit):
    n = len(digit)
    res, sol = [],[]

    letter = { '2':'abc', '3':'def', '4':'ghi', '5':'jkl',
               '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'
    }

    def backtrack(i):
        if i == n:
            res.append(''.join(sol[:]))
            return

        for num in letter[digits[i]]:
            sol.append(num)
            backtrack(i+1)
            sol.pop()
    backtrack(0)
    return res

print(letterCombinations(digits))

# Time Complexity: O(4^n)
# Space Complexity: O(n)
# The time complexity is O(4^n) because there are 4 possible letters for each digit (except for 7 and 9 which have 3 and 4 respectively).
