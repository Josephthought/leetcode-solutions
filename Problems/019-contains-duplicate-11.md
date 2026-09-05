# 219. Contains Duplicate II

**Pattern:** Hash Map (index tracking)

## Idea
Check if there are two equal elements within distance k of each other in
the array. Similar to the original Contains Duplicate, but a plain hash
set isn't enough this time — we also need to know HOW FAR APART the
duplicates are. Use a hash map instead, storing each number's most recent
index. When a number repeats, calculate the distance between the current
index and the last seen index; if it's within k, return True.

## Key formula
seen = {}
for i, num in enumerate(nums):
    if num in seen:
        dist = i - seen[num]
        if dist <= k:
            return True
    seen[num] = i
return False

## Complexity
- Time: O(n) — single pass through the array
- Space: O(n) — worst case, the dictionary holds one entry per unique
  number, so it can grow up to size n (unlike some earlier problems,
  this one genuinely needs O(n) space, no O(1) trick available)

## Gotcha
`seen[num] = i` must run EVERY iteration, not just when a duplicate is
found — otherwise the first occurrence of a number never gets recorded,
and it can never be matched against later. Also watch the comparison:
it's `<=` (at most k), not `==` (exactly k).