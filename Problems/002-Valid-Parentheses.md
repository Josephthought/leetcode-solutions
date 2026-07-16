# 20. Valid Parentheses

**Pattern:** Stack

## Idea
Check if brackets ( ) [ ] { } are properly opened and closed in order.
Every closing bracket must match the most recently opened bracket — that
"most recent" behavior is exactly what a stack gives you (Last In, First Out).

## Key formula
if char is an opening bracket: push it onto the stack
if char is a closing bracket: pop the stack and check it matches
at the end, the stack must be empty

## Complexity
- Time: O(n) — single pass through the string
- Space: O(n) — worst case, all characters are opening brackets

## Gotcha
Don't forget to check the stack isn't empty before popping (a closing
bracket with nothing open should fail), and check the stack is empty
at the very end (unclosed opening brackets should also fail).