# 70. Climbing Stairs

**Pattern:** Dynamic Programming (Fibonacci)

## Idea
You can climb 1 or 2 steps at a time — count how many distinct ways to
reach the top of an n-step staircase. The last move to reach step n is
either a 1-step from step (n-1), or a 2-step from step (n-2). So the total
ways to reach n is the sum of the ways to reach the two steps before it:
ways(n) = ways(n-1) + ways(n-2). This is the Fibonacci sequence in disguise.
Instead of storing the whole sequence, track just the last two values and
slide them forward each step.

## Key formula
if n == 1: return 1
prev2, prev1 = 1, 2  # ways(1), ways(2)
for i in range(3, n + 1):
    current = prev1 + prev2
    prev2 = prev1
    prev1 = current
return prev1

## Complexity
- Time: O(n) — one pass from 3 up to n
- Space: O(1) — only a fixed handful of variables (prev2, prev1, current),
  none of which grow with n

## Gotcha
Handle n == 1 as a special case before the loop — the sliding-box setup
assumes at least ways(1) and ways(2) exist, and would break or give the
wrong answer without this check.