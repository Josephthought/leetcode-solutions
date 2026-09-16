# 682. Baseball Game

**Pattern:** Stack

## Idea
Process a list of scoring operations and return the total score. Use a
stack (a list) to track running scores: a number gets pushed directly,
"C" removes the last score, "D" pushes double the last score, and "+"
pushes the sum of the last two scores. A stack fits naturally here since
every operation only cares about the most recent one or two entries.

## Key formula
stack = []
for i in operations:
    if i.lstrip('-').isdigit():
        stack.append(int(i))
    elif i == "C":
        stack.pop()
    elif i == "D":
        stack.append(stack[-1] * 2)
    elif i == "+":
        stack.append(stack[-1] + stack[-2])
return sum(stack)

## Gotcha
Use i.lstrip('-').isdigit() instead of just i.isdigit() — negative score
strings like "-5" would otherwise be misidentified as not a number, since
isdigit() returns False when a minus sign is present.

## Complexity
- Time: O(n) — single pass through operations, constant work per operation
- Space: O(n) — worst case (all operations are numbers), stack grows to
  hold up to n scores