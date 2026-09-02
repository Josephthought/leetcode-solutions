# 141. Linked List Cycle

**Pattern:** Fast & Slow Pointers (Floyd's Cycle Detection)

## Idea
Determine if a linked list loops back on itself instead of ending at None.
Walking with a single pointer would run forever if a cycle exists, so use
two pointers starting at the head: `slow` moves 1 step at a time, `fast`
moves 2 steps at a time. Think of two runners on a circular track — if
there's a loop, the faster one eventually laps the slower one and they land
on the same node. If there's no cycle, `fast` simply reaches the end (None)
first, since the list has a genuine end.

## Key formula
slow = head
fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
        return True
return False

## Complexity
- Time: O(n) — even in the worst case, fast gains one step on slow each
  round, so they meet within at most n total steps
- Space: O(1) — only two pointer variables, no extra data structure

## Gotcha
Check `while fast and fast.next` (not just `while fast`) — since fast
moves two steps at a time, you need to confirm both fast AND fast.next
exist before jumping, or you'll crash trying to access `.next` on None.