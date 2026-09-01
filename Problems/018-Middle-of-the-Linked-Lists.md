# 876. Middle of the Linked List

**Pattern:** Fast & Slow Pointers

## Idea
Find the middle node of a linked list (if two middles, return the second).
Reuses the same fast/slow pointer setup from Linked List Cycle: `slow`
moves 1 step at a time, `fast` moves 2 steps at a time, both starting at
head. Since fast moves twice as fast, by the time fast has covered the
whole list, slow has only covered half of it — landing exactly on the
middle. No need to know the list's length in advance.

## Key formula
slow = head
fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
return slow

## Complexity
- Time: O(n) — fast covers the list in one pass (~n/2 iterations for slow)
- Space: O(1) — only two pointer variables

## Gotcha
Same as Linked List Cycle: check `while fast and fast.next` (not just
`while fast`) — fast moves two steps at a time, so both need to exist
before jumping, or you'll crash on `.next` of None.