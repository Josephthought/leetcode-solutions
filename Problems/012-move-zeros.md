# 283. Move Zeroes

**Pattern:** Two Pointers (in-place array manipulation)

## Idea
Move all zeros in the array to the end, while keeping the relative order of
non-zero elements — and do it in-place (no new array). Use a "slot" pointer
that tracks the next position where a non-zero value should go. Walk through
the array once: every time you find a non-zero number, copy it into `slot`
and advance `slot`. After that pass, everything from `slot` to the end of
the array is leftover/stale — fill those positions with 0.

## Key formula
slot = 0
for i in range(len(nums)):
    if nums[i] != 0:
        nums[slot] = nums[i]
        slot += 1

for j in range(slot, len(nums)):
    nums[j] = 0

## Complexity
- Time: O(n) — two separate single passes (O(n) + O(n) simplifies to O(n))
- Space: O(1) — only the `slot` variable, no new array created

## Gotcha
Don't forget the second loop! The first pass only places non-zero values
correctly at the front — it doesn't clean up the leftover values still
sitting in the tail positions. Without the second loop, duplicates remain
instead of zeros.