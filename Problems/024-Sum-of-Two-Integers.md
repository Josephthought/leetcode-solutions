# 371. Sum of Two Integers

**Pattern:** Bit Manipulation (add without + or -)

## Idea
Add two integers without using + or -. Think of adding two binary numbers
by hand: at each bit position there is a digit result and a possible carry.
- XOR (a ^ b) gives the sum of each bit WITHOUT the carry
- AND (a & b) shows where both bits are 1, which is exactly where a carry
  happens
- Shift that carry left by 1 ((a & b) << 1) to move it into the next
  position, where it needs to be added
Repeat: the XOR result becomes the new a, the shifted carry becomes the new
b, until there is no carry left (b == 0). Then a holds the final sum.

## Key formula
while b != 0:
    carry = a & b
    a = a ^ b
    b = carry << 1
return a

## Worked example (a = 2, b = 3)
Round 1: a = 010, b = 011 -> carry = 010, a = 001, b = 100
Round 2: a = 001, b = 100 -> carry = 000, a = 101, b = 000
b is 0, so stop. a = 101 = 5.

## Complexity
- Time: O(1) — the carry can only shift through a fixed number of bit
  positions (about 32), so the loop is bounded by bit-width, not by the
  size of the input values
- Space: O(1) — only a few variables (a, b, carry)

## Gotcha
Remember `carry = a & b` needs the = sign (easy to forget when writing
quickly). Also, this loop is bounded by the fixed bit-width of integers,
which is why it counts as O(1) even though it is a while loop. (Python
integers have no fixed width, so LeetCode's Python version can loop
forever on some negative inputs without a 32-bit mask, but your accepted
solution passed as written.)