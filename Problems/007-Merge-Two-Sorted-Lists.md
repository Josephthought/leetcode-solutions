# 21. Merge Two Sorted Lists

**Pattern:** Linked List

## Idea
Merge two already-sorted linked lists into one sorted list. Use a dummy
head node to simplify edge cases, then walk both lists at once, always
attaching the smaller current node next.

## Key formula
while list1 and list2:
    if list1.val <= list2.val: attach list1, advance list1
    else: attach list2, advance list2
attach whichever list still has leftover nodes

## Complexity
- Time: O(m + n) — where m, n are the lengths of the two lists
- Space: O(1) — reusing existing nodes, not creating new ones

## Gotcha
Use a dummy/placeholder head node so you don't have to write special
logic for "what's the very first node" — makes the code much cleaner.