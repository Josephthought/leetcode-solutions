# LeetCode #217 - Contains Duolicate
# Difficulty: Easy
# Time: 0(n) |Space: 0(n)
# Solved: March 2026

class Solution:
  def containsDuplicate(self, nums):

    seen = set()

    for num in nums:
      if num in seen:
        return True
      else:
        seen.add(num)

    return False
