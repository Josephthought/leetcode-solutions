# 704. Binary Search

**Pattern:** Binary Search

## Idea
Find a target value in a SORTED array efficiently by repeatedly cutting
the search space in half instead of checking every element one by one.

## Key formula
left, right = 0, len(nums) - 1
while left <= right:
    mid = (left + right) // 2
    if nums[mid] == target: return mid
    elif nums[mid] < target: left = mid + 1
    else: right = mid - 1
return -1

## Complexity
- Time: O(log n) — search space halves each step
- Space: O(1) — only a few index variables

## Gotcha
This only works on a SORTED array — binary search on unsorted data
gives wrong results.