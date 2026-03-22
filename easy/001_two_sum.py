#LeetCode #1 _ Two Sum
#Difficulty: Easy
#Time:0(n) | Space: 0(n)
#Solved: March 2026

class Solution:
  def twoSum(self, nums, target):
    seen = {}

    for i, num in enumerate(nums):
      complement = target - num

      if complement in seen:
        return[seen[complement], i]

      seen[num] = i
    
