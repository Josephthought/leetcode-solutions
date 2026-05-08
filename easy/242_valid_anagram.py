# Leetcode #242 - Valid Anagram
#Difficulty: Easy
#Time: 0(n) | space: 0(n)
#solved: 2026

class Solution:
    def isAnagram(self, s, t):
        

        if len(s) != len(t):
            return False 

        count_s = {}
        for char in s:
            count_s[char] = count_s.get(char, 0) + 1

        count_t = {}
        for char in t:
            count_t[char] = count_t.get(char, 0) + 1

        return count_s == count_t
