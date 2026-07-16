# 53. Maximum Subarray

**Pattern:** Kadane's Algorithm (Dynamic Programming)

## Idea
Find the largest sum of any contiguous subarray. Brute force checks every
start/end pair — O(n²). Kadane's trick: keep a running sum, and if it ever
goes negative, drop it and restart from the current number, since a negative
sum only drags future sums down.

## Key formula
current_sum = max(nums[i], current_sum + nums[i])
max_sum = max(max_sum, current_sum)

## Complexity
- Time: O(n) — single pass
- Space: O(1) — only two variables, doesn't grow with input

## Gotcha
Don't forget to update max_sum on every iteration, not just when current_sum resets.