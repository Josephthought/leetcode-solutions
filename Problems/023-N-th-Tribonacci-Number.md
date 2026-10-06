# 1137. N-th Tribonacci Number

**Pattern:** Dynamic Programming (Fibonacci-style, extended to 3 terms)

## Idea
Like Fibonacci, but each number depends on the THREE numbers before it
instead of two: T(n) = T(n-1) + T(n-2) + T(n-3). Base cases T(0)=0, T(1)=1,
T(2)=1 are known values, not calculated. For n > 2, use three sliding boxes
(a, b, c) holding the three most recent values. Each step, compute the next
value as their sum, then slide all three boxes forward (a=b, b=c, c=new) to
prepare for the next round — no need to store the whole sequence.

## Key formula
if n <= 2:
    base = [0, 1, 1]
    return base[n]

a, b, c = 0, 1, 1
for i in range(3, n + 1):
    new = a + b + c
    a, b, c = b, c, new
return c

## Complexity
- Time: O(n) — one pass from 3 up to n
- Space: O(1) — only a fixed handful of variables (a, b, c, new), none of
  which grow with n

## Gotcha
range(3, n + 1) needs the +1 — range() excludes its stop value by default,
so without it the loop would stop one step short and miss computing T(n)
itself.