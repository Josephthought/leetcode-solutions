# 136. Single Number

**Pattern:** XOR / Bit Manipulation

## Idea
Every number in the array appears exactly twice, except one number that
appears once. A hash map can solve this by counting occurrences, but it
uses O(n) space. The optimal trick uses XOR: XOR every number in the array
together in one pass. Two key facts make this work:
- Any number XORed with itself is 0 (a ^ a = 0)
- Any number XORed with 0 stays the same (a ^ 0 = a)

Since XOR doesn't care about order, every pair of duplicate numbers cancels
itself out to 0, leaving only the number that had no pair.

## Key formula
result = 0
for num in nums:
    result = result ^ num
return result

## Complexity
- Time: O(n) — single pass through the array
- Space: O(1) — only one variable (`result`), doesn't grow with input

## Gotcha
This only works because EVERY number except one appears exactly twice.
If numbers could appear three or more times, this trick breaks down and
you'd need a different approach (like a hash map with counts).