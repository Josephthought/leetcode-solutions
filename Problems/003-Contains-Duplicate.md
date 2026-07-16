# 217. Contains Duplicate

**Pattern:** Hash Set

## Idea
Check if any value appears more than once in the array. Brute force compares
every pair — O(n²). Better: use a hash set to track numbers you've already
seen. If you hit a number that's already in the set, you found a duplicate.

## Key formula
if num in seen: return True
seen.add(num)

## Complexity
- Time: O(n) — single pass
- Space: O(n) — set can hold up to n entries

## Gotcha
A set only stores unique values automatically — that's what makes the
"have I seen this before" check O(1) instead of scanning a list each time.