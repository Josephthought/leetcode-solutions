# 242. Valid Anagram

**Pattern:** Hash Map (frequency counting)

## Idea
Check if two strings use exactly the same letters the same number of times.
Count the frequency of each character in both strings and compare the counts.

## Key formula
count = {}
for char in s: count[char] = count.get(char, 0) + 1
for char in t: count[char] = count.get(char, 0) - 1
all values in count must equal 0 at the end

## Complexity
- Time: O(n) — single pass through each string
- Space: O(1) — at most 26 letters (English alphabet), so the map size
  doesn't grow with input length

## Gotcha
Check the strings are the same length first — if not, they can't be
anagrams, and it saves you a wasted pass.