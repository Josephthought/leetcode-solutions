# 206. Reverse Linked List

**Pattern:** Linked List

## Idea
Reverse the direction of every pointer in a singly linked list. Walk
through the list once, and at each node, flip its `next` pointer to
point backward instead of forward.

## Key formula
prev = None, curr = head
while curr:
    next_temp = curr.next
    curr.next = prev
    prev = curr
    curr = next_temp
return prev

## Complexity
- Time: O(n) — single pass through the list
- Space: O(1) — just a few pointer variables, no new list created

## Gotcha
Save `curr.next` in a temp variable BEFORE overwriting it — otherwise
you lose the rest of the list once you reverse the pointer.