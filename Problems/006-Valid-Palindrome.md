# 125. Valid Palindrome

**Pattern:** Two Pointers

## Idea
Check if a string reads the same forwards and backwards, ignoring
non-alphanumeric characters and case. Use two pointers starting at
both ends, moving inward, skipping invalid characters, and comparing.

## Key formula
left = 0, right = len(s) - 1
while left < right:
    skip non-alphanumeric chars on both sides
    if s[left].lower() != s[right].lower(): return False
    left += 1, right -= 1

## Complexity
- Time: O(n) — each pointer moves through the string once
- Space: O(1) — no extra data structure, just two index variables

## Gotcha
Remember to lowercase both characters before comparing — 'A' and 'a'
should count as a match.