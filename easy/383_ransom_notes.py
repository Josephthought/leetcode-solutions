class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        count_1 = {}
        for char in ransomNote:
            count_1[char] = count_1.get(char, 0) + 1

        count_2 = {}
        for char in magazine:
            count_2[char] = count_2.get(char, 0) + 1

        for char in ransomNote:
            if char not in count_2 or count_2[char] < count_1[char]:
                return False

        return True