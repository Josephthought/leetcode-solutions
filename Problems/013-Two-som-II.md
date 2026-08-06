# 167. Two Sum II - Input Array Is Sorted

**Pattern:** Two Pointers

## Idea
Given a sorted array, find two numbers that add up to a target and return
their (1-indexed) positions. Since the array is sorted, use two pointers —
one at the start (`left`), one at the end (`right`) — instead of a hash map.
Compare their sum to the target: if too big, move `right` backward (swap
out the largest number for something smaller); if too small, move `left`
forward (swap out the smallest number for something bigger). This narrows
the search from both ends until the target is found.

## Key formula
left, right = 0, len(numbers) - 1
while left < right:
    total = numbers[left] + numbers[right]
    if total == target: return [left + 1, right + 1]
    elif total < target: left += 1
    else: right -= 1

## Complexity
- Time: O(n) — left and right move toward each other, together taking at
  most n total steps before crossing
- Space: O(1) — just the two pointer variables, no hash map needed

## Gotcha
Remember to return 1-indexed positions (`left + 1`, `right + 1`), not the
raw 0-indexed values — LeetCode is specific about this on this problem,
unlike the original Two Sum.