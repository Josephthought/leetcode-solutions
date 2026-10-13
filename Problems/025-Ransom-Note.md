# 383. Ransom Note

**Pattern:** Hash Map (frequency counting)

## Idea
Check whether ransomNote can be built from the letters in magazine, where
each magazine letter can be used only once. Same frequency-counting idea as
Valid Anagram: count how many of each letter the note needs, count how many
of each letter the magazine has, then check every letter the note needs. If
the magazine has fewer of any letter than the note requires (or lacks it
entirely), return False. If every letter passes, return True.

## Key formula
count_1 = {}
for char in ransomNote:
    count_1[char] = count_1.get(char, 0) + 1

count_2 = {}
for char in magazine:
    count_2[char] = count_2.get(char, 0) + 1

for char in ransomNote:
    if char not in count_2 or count_2[char] < count_1[char]:
        return False
return True

## Complexity
- Time: O(m + n) — three loops that run one after another (not nested),
  so their steps add: m + n + m, which simplifies to O(m + n)
- Space: O(1) — each dictionary holds at most 26 keys (lowercase letters),
  no matter how long the strings are

## Gotcha
Loop over ransomNote (what is NEEDED) in the final check, not magazine, and
compare available against needed: `count_2[char] < count_1[char]` means
"not enough in the magazine". Also, return True only AFTER the loop ends,
and use return False inside it, instead of a flag variable you never return.
Nested loops multiply (O(n²)), sequential loops add (O(m + n)).