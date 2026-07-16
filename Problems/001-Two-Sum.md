# 1. Two Sum

**Pattern:** Hash Map

## Idea
Find two numbers in the array that add up to a target, return their indices.
Brute force checks every pair — O(n²). Better: as you loop through once, store
each number's index in a hash map. For each number, check if (target - number)
already exists in the map — if so, you found your pair instantly.

## Key formula
complement = target - nums[i]
if complement in seen: return [seen[complement], i]
seen[nums[i]] = i

## Complexity
- Time: O(n) — single pass
- Space: O(n) — hash map can hold up to n entries

## Gotcha
Check for the complement BEFORE adding the current number to the map,
so you don't accidentally match a number with itself.