python# LeetCode #20 - Valid Parentheses
# Difficulty: Easy
# Time: O(n) | Space: O(n)
# Solved: March 2026
# Runtime: beats 100%
```
class Solution:
    def isValid(self, s):
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        stack = []

        for char in s:
            if char in pairs:
                if stack and stack[-1] == pairs[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0
