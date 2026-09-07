# 190. Reverse Bits

**Pattern:** Bit Manipulation

## Idea
Reverse the order of bits in a 32-bit unsigned integer. Build a new number
one bit at a time by grabbing the last bit off the original number and
stacking it onto a result — like unloading plates from one pile onto
another, reversing the order. Repeat this exactly 32 times (since it's
always a 32-bit number, regardless of the input's actual value).

Each round:
1. Grab the last bit of n using `n & 1`
2. Shift result left to make room for the new bit: `result << 1`
3. Drop the grabbed bit into that empty slot with OR: `| bit`
4. Shift n right to drop the bit we already used: `n = n >> 1`

## Key formula
result = 0
for i in range(32):
    bit = n & 1
    n = n >> 1
    result = (result << 1) | bit
return result

## Complexity
- Time: O(1) — the loop always runs exactly 32 times, regardless of the
  value of n; it doesn't scale with input size
- Space: O(1) — only a few fixed variables (result, bit, i)

## Gotcha
Don't reuse `n` as the loop counter variable name (e.g. `for n in
range(32)`) — that overwrites the actual input number you're trying to
reverse. Use a different name like `i` for the loop counter.