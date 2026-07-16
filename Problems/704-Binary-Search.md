# 704. Binary Search

## Difficulty

Easy

---

## Pattern

Binary Search

---

## LeetCode Link

https://leetcode.com/problems/binary-search/

---

## Key Idea

The array must be sorted.

Instead of checking every element one by one, repeatedly eliminate half of the remaining search space.

---

## Variables Used

- start
- end
- mid

---

## Algorithm

1. Set `start = 0`
2. Set `end = len(nums) - 1`
3. While `start <= end`
4. Calculate `mid`
5. Compare `nums[mid]` with `target`
6. If equal → return `mid`
7. If target is larger → move `start`
8. If target is smaller → move `end`
9. If loop finishes → return `-1`

---

## Time Complexity

O(log n)

### Why?

Every comparison removes half of the remaining search space.

Example:

16 → 8 → 4 → 2 → 1

---

## Space Complexity

O(1)

### Why?

Only three variables are used:

- start
- end
- mid

No extra arrays are created.

---

## Mistakes I Made

- Initialized `end` as `len(nums)` instead of `len(nums) - 1`.
- Calculated `mid` outside the loop.
- Forgot the `target` parameter.
- Put the `while` loop outside the function because of indentation.
- Tried to write `else nums[mid] == target`.
- Initially thought `while start < end` instead of `while start <= end`.

---

## What I Learned

- Binary search only works on a sorted array.
- `mid` must be recalculated every iteration.
- Never create new arrays; move the boundaries instead.
- Think in terms of indices (`start`, `end`, `mid`) instead of slicing lists.

---

## Confidence

⭐⭐⭐⭐☆