#LeetCode #1 _ Two Sum
#Difficulty: Easy
#Time:0(n) | Space: 0(n)
#Solved: june 2026

import re
class Solution:
    def isPalindrome(self, s):
        s = s.lower()
        s = re.sub(r'[^a-zA-Z0-9]', '', s)

        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left +=1
            right -= 1

        return True
